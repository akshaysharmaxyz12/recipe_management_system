This is a web application built with Flask that allows users to share and manage recipes. Users can add new recipes, edit existing ones, and delete recipes. The application also includes a login system for user authentication.

Features
User Authentication: Users can sign up, log in, and log out securely.
Recipe Management: Users can add, edit, and delete recipes.
Scraping Data: The application scrapes data from a specified URL and adds it to the database.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/recipe-sharing-platform.git
Install the required dependencies:

Copy code
pip install -r requirements.txt
Set up the database:

Ensure you have MySQL installed and running.
Create a MySQL database named akshay or use an existing one.
Modify the database connection details in the app.py file if necessary.
Run the application:

Copy code
python app.py
Access the application in your web browser at http://localhost:5000.

Usage
Sign Up: If you're a new user, sign up for an account.
Log In: Log in with your credentials.
View Recipes: Browse through the list of available recipes on the homepage.
Add Recipe: Click on the "Add Recipe" button to add a new recipe.
Edit Recipe: To edit a recipe, click on the "Edit" button next to the recipe.
Delete Recipe: To delete a recipe, click on the "Delete" button next to the recipe.
Credits
This application uses the following technologies:

Flask
MySQL
BeautifulSoup (for web scraping)
