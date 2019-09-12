
from flask import Flask, render_template, request, url_for
import requests
import os
import urllib.request as ur,json
import json

app = Flask(__name__)


# define a function that searches the Giphypop API with the giphypop library


# represents home page
@app.route('/')
def index():
    return render_template('index.html')  # points to index.html page


@app.route('/gif', methods=["GET"])
def make_gif():
    # data=json.loads(s.urlopen("http://api.giphy.com/v1/gifs/search?q=nerdy&api_key=RszCWrqNToHdZUk9E2o7f2TPk5Srv6y4&q&limit=40&offset=0&rating=G&lang=en").read())
    # return json.dumps(data, sort_keys=True, indent=4)
    search_term = request.args.get('search-term')

    response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=RszCWrqNToHdZUk9E2o7f2TPk5Srv6y4&q={search_term}&limit=25&offset=0&rating=G&lang=en')
    # helped by IKE and Medi
    images = json.loads(response.text)['data']
    urls = [image['images']['fixed_width']['url'] for image in images]
    
    return render_template('gif.html', urls=urls)





if __name__ == "__main__":
    app.run(debug=True, port=8080)
