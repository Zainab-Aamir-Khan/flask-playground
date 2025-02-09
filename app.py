from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return render_Template("index.html")

@app.route("/products")
def products():
    return "this is a product's page"


if __name__ == "__main__":
    app.run(debug=True)