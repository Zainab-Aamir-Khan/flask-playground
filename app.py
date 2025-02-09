from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(500), nullable= False)
    date_created = db.Column(db.DateTime, default = datetime.now)

    def __repr__(self) -> str:
        return f"{self.id} - {self.title}"
    

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    Todo = todo(title = 'First todo', description = "Invest in Python company")
    db.session.add(todo)
    db.session.commit()
    return render_template("index.html")

@app.route("/products")
def products():
    return "this is a product's page"


if __name__ == "__main__":
    app.run(debug=True)