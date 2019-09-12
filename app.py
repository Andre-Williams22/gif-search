
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
 
    search_term = request.args.get('search-term')

    response = requests.get(f'https://api.tenor.com/v1/search?q={search_term}&key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(response.content)
        return top_10gifs
    else:
        top_10gifs = None
    '''
    images = json.loads(response.text)

    urls = [image['images']['fixed_width']['url'] for image in images

    return render_template('gif.html', response=response)
    #images = json.loads(response.text)['data']
    # creates a list of urls and thier fixed images
    #urls = [image['images']['fixed_width']['url'] for image in images]'''





if __name__ == "__main__":
    app.run(debug=True, port=8080)
