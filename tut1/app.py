from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return ''' 
            <h1>Hello World</h1>
            <button><a href="/hello">Click here</a></button>
            '''
@app.route('/hello')
def hello():
    return '''Hey there 
            <button><a href="/">Go back</a></button>
            '''

if __name__=='__main__':
    app.run(debug=True)