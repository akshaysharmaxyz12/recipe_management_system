This is a web-based Recipe Management System built with Flask and MySQL.

## Features

- Users can view, add, edit, and delete recipes.
- User authentication system for login and signup.
- Responsive design for optimal viewing on various devices.
- Integration with MySQL database for storing recipe data.

## Technologies Used

- Flask
- MySQL
- HTML
- CSS (Bootstrap for styling)
- JavaScript

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/akshaysharmaxyz12/recipe_management_system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd recipe_management_system
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
   
   - Create a MySQL database named `akshay`.
   - Import the database schema from the `database.sql` file provided.

5. Update the database connection settings in `app.py`:

    ```python
    # Update the database connection settings
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="akshay"
    )
    ```

6. Run the Flask application:

    ```bash
    flask run
    ```

7. Access the application in your web browser at `http://localhost:5000`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
