
from flask import Flask, render_template, request, url_for
import requests
import os
import urllib.request as ur
import json
import json

app = Flask(__name__)


# represents home page
@app.route('/')
def index():
    return render_template('index.html')  # points to index.html page


if __name__ == "__main__":
    app.run(debug=True, port=8080)
