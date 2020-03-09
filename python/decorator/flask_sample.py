from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/blog")
def about():
    return "blogs here"


if __name__ == "__main__":
    app.run()