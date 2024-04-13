```markdown
# Flask User Authentication System

This Flask application provides a basic user authentication system using SQLAlchemy for database management and bcrypt for password hashing.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ro706/flask-tut.git flask
   ```

2. Navigate into the project directory:
   ```bash
   cd flask
   ```


## Configuration

- **Database Configuration**: The application is configured to use SQLite database by default. You can modify the database URI in the `app.config['SQLALCHEMY_DATABASE_URI']` parameter in `app.py` if you want to use a different database.

- **Secret Key**: Update the `app.secret_key` parameter in `app.py` with a secret key for securing the session.

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Access the application in your web browser at `http://localhost:5000`.

3. You can register a new user by accessing `/register` route.

4. After registration, you can log in using the `/login` route.

5. Upon successful login, you'll be redirected to the dashboard at `/dashboard`.

6. You can log out using the `/logout` route.

## Files

- `app.py`: Main Flask application file containing the routes and database models.
- `templates/`: Directory containing HTML templates for the application.
  - `index.html`: Home page template.
  - `register.html`: User registration page template.
  - `login.html`: User login page template.
  - `dashboard.html`: Dashboard page template.

## Dependencies

- Flask: Web framework for Python.
- Flask-SQLAlchemy: Flask extension for SQLAlchemy integration.
- bcrypt: Library for password hashing.

## Contributors

- [ Ro706 ](https://github.com/Ro706)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to modify it according to your preferences and project specifics!

```

## Image 
![Screenshot 2024-04-14 011035](https://github.com/Ro706/flask_tut/assets/60247178/3dd5d13e-9554-48e1-82c7-6457e25e3db5)
![Screenshot 2024-04-14 011107](https://github.com/Ro706/flask_tut/assets/60247178/c0bd5ca0-8768-4092-9db2-d15d39d96ce7)
![Screenshot 2024-04-14 011124](https://github.com/Ro706/flask_tut/assets/60247178/28df23cd-911c-4a38-a1e2-14cc4ca315fb)


