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

    results = top_ten()
    list_of_gifs = results['results']

    # points to index.html page
    return render_template('index.html', list_of_gifs=list_of_gifs)


@app.route('/gif', methods=['GET'])
def make_gif():

    search_term = request.args.get('search-term')
    print(search_term)

    response = requests.get(
        f'https://api.tenor.com/v1/search?q={search_term}&key=1F2TY5LFTDOH&limit=10')

    if response.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(response.content)
        # print(top_10gifs['results'])
        return render_template('index.html', list_of_gifs=top_10gifs['results'], search_term=search_term)
    else:
        top_10gifs = None

@app.route('/sports', methods=['GET', 'POST'])
def sports():
    # set the apikey and limit
    apikey = "LIVDSRZULELA"  # test value
    lmt = 10

    # our test search
    search_term = "sports"

    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        sports = json.loads(r.content)
        return render_template('sports.html', list_or_gifs=sports['results'])
    else:
        sports = None



# get the top 10 trending GIFs - using the default locale of en_US

def top_ten():
    r = requests.get(
        "https://api.tenor.com/v1/trending?key=1F2TY5LFTDOH&limit=10")

    if r.status_code == 200:
        trending_gifs = json.loads(r.content)
    else:
        trending_gifs = None

    return trending_gifs


if __name__ == "__main__":
    app.run(debug=True, port=8080)
