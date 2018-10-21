from flask import Flask
from flask import render_template as rt
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = 'Hello, World!'
    return rt("test.html", msg=msg)
    