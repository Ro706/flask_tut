```markdown
# Simple Todo Web Application

This is a simple Todo web application built using Flask, a lightweight Python web framework, and SQLAlchemy, a Python SQL toolkit and Object-Relational Mapper.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Ro706/flask_tut.git
   ```

2. Navigate to the project directory:
   ```bash
   cd flask_tut
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

## Features

- Add new todo items.
- Mark todo items as completed.
- Delete todo items.

## File Structure

- `app.py`: Contains the main Flask application code.
- `templates/index.html`: HTML template for rendering the todo list.
- `todo.db`: SQLite database file.

## Usage

- Upon running the application, open a web browser and go to `http://localhost:5000`.
- You will see a form to add new todo items. Enter the task and press Enter or click on the "Add" button.
- Existing todo items will be displayed below the form.
- To mark an item as completed, click on the checkbox next to it.
- To delete an item, click on the "Delete" button next to it.

## Dependencies

- Flask: A micro web framework for Python.
- Flask-SQLAlchemy: Provides integration between Flask and SQLAlchemy.
- SQLAlchemy: SQL toolkit and Object-Relational Mapper for Python.

## Database

This application uses SQLite as its database. The database file (`todo.db`) will be created in the project directory upon running the application for the first time. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
