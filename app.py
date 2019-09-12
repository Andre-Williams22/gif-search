
from flask import Flask, render_template, request, url_for
import requests
import os
import urllib.request as ur
import json
import json

app = Flask(__name__)


# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# User's searched gif
@app.route('/gif', methods=["POST"])
def make_gif():
    params = {
        "q": 'fun',
        "Key": "1F2TY5LFTDOH"
    }

    userInput = request.form['search-term']
    processedText = userInput.upper()

    response = requests.get(
        'https://api.tenor.com/v1/search',
        params=params)

    return render_template('gif.html', response=response, processedText=processedText)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
