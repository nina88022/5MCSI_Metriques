from flask import Flask, rendertemplatestring, rendertemplate, jsonify
from flask import rendertemplate
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(name)

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/')
def hello_world():
    return render_template('hello.html') #comment2


if __name == "__main":
  app.run(debug=True)
