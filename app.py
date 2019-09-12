
from flask import Flask, render_template, request, url_for
import requests
import os
import urllib.request as ur,json
import json

app = Flask(__name__)


# represents home page
@app.route('/')
def index():
    return render_template('index.html')  # points to index.html page


@app.route('/gif', methods=["GET"])
def make_gif():
    params = {
    "q": 'fun',
    "Key": "1F2TY5LFTDOH"
}
    response = requests.get(
        'https://api.tenor.com/v1/search',
        params=params)
  
    #images = json.loads(response.text)['data']
    # creates a list of urls and thier fixed images
    #urls = [image['images']['fixed_width']['url'] for image in images]
    
    return render_template('gif.html', urls=urls)





if __name__ == "__main__":
    app.run(debug=True, port=8080)
