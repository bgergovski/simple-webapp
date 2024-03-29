from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/members")
def members():
    return "Members"


@app.route("/members/<string:name>/")
def getmember(name):
    return name


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
