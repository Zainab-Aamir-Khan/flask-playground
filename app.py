from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/products")
def products():
    return "this is a product's page"


if __name__ == "__main__":
    app.run(debug=True)