from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tut4.db'
db = SQLAlchemy(app)

class tut_name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))

    # Represents a single instance of the `tut_name` table in the database.

    def __repr__(self):
        """Returns a string representation of a `tut_name` instance.

        Returns:
            str: A string in the format '<tut_name {self.id}>', where {self.id} is the id of the instance.
        """
        return f'<tut_name {self.id}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name.strip() != '':
            new_name = tut_name(content=name)
            db.session.add(new_name)
            db.session.commit()
        return redirect('/')
    else:
        names = tut_name.query.all()
        return render_template('index.html', names=names)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        name = tut_name.query.get(id)
        if name is None:
            return "Name not found", 404
        db.session.delete(name)
        db.session.commit()
        return redirect('/')
    else:
        # Handle GET request, maybe display a confirmation page
        return redirect('/')
if __name__ == '__main__':
    # Creating the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
