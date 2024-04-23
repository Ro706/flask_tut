from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return ''' 
            <h1>Hello World</h1>
            <button><a href="/hello">Click here</a></button>
            '''
# @app.route('/hello')
def hello():
    return '''Hey there 
            <button><a href="/">Go back</a></button>
            '''
    # app.add_url_rule('/', 'helloworld', hello_world)
if __name__=='__main__':
    app.run(debug=True)
    app.add_url_rule('/', 'hello', hello)