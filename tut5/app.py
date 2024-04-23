from flask import Flask

app = Flask(__name__)

def hello_world():
    return "Hello, Ro706!"

# Register the URL rule
app.add_url_rule('/', 'helloworld', hello_world)

if __name__ == '__main__':
    app.run(debug=True)
