# Flask Hello World

This is a simple Flask application that demonstrates basic routing functionality. When you run the application, it starts a Flask server that listens for incoming HTTP requests. The routes defined in the application determine how the server responds to different URLs.

## Prerequisites

Make sure you have Python and Flask installed on your system before running this application.

## Installation

1. Clone this repository or download the source code.
2. Navigate to the directory where the code is located.
3. Install Flask if you haven't already:

    ```bash
    pip install Flask
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the homepage.

3. Click the "Click here" button to navigate to the `/hello` route.

4. Click the "Go back" button to return to the homepage.

## Code Explanation

- The Flask `Flask` class is imported to create the application instance.
- Two routes are defined using the `@app.route()` decorator. 
    - The `'/'` route is associated with the `index()` function, which returns a simple HTML page displaying "Hello World" and a button linking to the `/hello` route.
    - The `'/hello'` route is associated with the `hello()` function, which returns "Hey there" and a button linking back to the homepage.
- The `__name__` variable is used to ensure that the Flask application runs when the script is executed directly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
