from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import mysql.connector
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key of your choice

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2000",
    database="akshay"
)
cursor = conn.cursor()

# Function to scrape data and add it to the database
def scrape_and_add_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        if table:
            header = []
            data = []
            for row in table.find_all("tr"):
                for cell in row.find_all(["th"]):
                    text = cell.get_text(strip=True)
                    if ' ' in text:
                        text = f"`{text}`"
                    header.append(text)
                row_data = []
                for cell in row.find_all(["td"]):
                    text = cell.get_text(strip=True)
                    row_data.append(text)
                if row_data:
                    data.append(row_data)
            for items in data:
                query = "INSERT INTO `recipe sharing platform` ({}) VALUES ({})"
                query = query.format(', '.join(header), ', '.join(['%s'] * len(header)))
                cursor.execute(query, items)
                conn.commit()
            return True
        else:
            print("Table not found on the website.")
            return False
    else:
        print(f"Error: Request failed with status code {response.status_code}")
        return False

# Check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Home route - displays all recipes
@app.route('/get_recipe')
def index():
    cursor.execute("SELECT * FROM `recipe sharing platform`")
    recipes = cursor.fetchall()
    return render_template('index.html', recipes=recipes)

# Add recipe route - displays form to add a new recipe
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['Recipe']
        ingredients = request.form['Main Ingredients']
        source = request.form['Source or curriculum']
        query = "INSERT INTO `recipe sharing platform` (Recipe, `Main Ingredients`, `Source or curriculum`) VALUES (%s, %s, %s)"
        cursor.execute(query, (recipe_name, ingredients, source))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


# Delete recipe route - deletes a recipe
@app.route('/delete/<int:Recipe>', methods=['POST'])
@login_required
def delete_recipe(recipe):
    query = "DELETE FROM `recipe sharing platform` WHERE Recipe = %s"
    cursor.execute(query, (recipe,))
    conn.commit()
    return redirect(url_for('index'))

# Edit recipe route - displays form to edit a recipe
@app.route('/edit/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    if request.method == 'POST':
        new_recipe_name = request.form['Recipe']
        new_ingredients = request.form['Main Ingredients']
        new_instructions = request.form['Source or curriculum']
        query = "UPDATE `recipe sharing platform` SET Recipe = %s, Main Ingredients = %s, Source or curriculum = %s WHERE Recipe = %s"
        cursor.execute(query, (new_recipe_name, new_ingredients, new_instructions, recipe_id))
        conn.commit()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM `recipe sharing platform` WHERE Recipe = %s", (recipe_id,))
    recipe = cursor.fetchone()
    return render_template('edit.html', recipe=recipe)

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password.'
            return render_template('login.html', error=error)
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Sign up route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        phone_no = request.form['phone_no']
        age = request.form['age']
        name = request.form['name']
        password = generate_password_hash(request.form['password'])
        query = "INSERT INTO users (username, phone_no, age, name, password) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (email, phone_no, age, name, password))
            conn.commit()
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            error = 'Email or phone number'
    # Return a response for GET requests as well
    return render_template('signup.html')  # Adjust this line according to your template filename
