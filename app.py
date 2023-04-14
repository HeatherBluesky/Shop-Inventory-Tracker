from flask import Flask, render_template
from models.book import Book
from models.author import Author


app = Flask(__name__)

app.register_blueprint()

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)