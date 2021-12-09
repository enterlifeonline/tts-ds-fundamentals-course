from flask import Flask

app = Flask(__name__)

@app.route("/")
def demo():
    return "Hello, word! This is a test."
