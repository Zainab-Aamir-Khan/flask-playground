from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(500), nullable= False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.title}"
    

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about", methods =["GET", "POST"])
def about():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        new_todo = Todo(title = 'First todo', description = "Invest in Python company")
        db.session.add(new_todo)
        db.session.commit()
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template("index.html", allTodo = allTodo)

@app.route("/show")
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "this is a showpiece page"

@app.route("/products")
def products():
    return "this is a product's page"


if __name__ == "__main__":
    app.run(debug=True)