import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def make_joke():
    params = {"gifs": 'faces',
              "Key": "1F2TY5LFTDOH"}
    response = requests.get(
        'https://api.tenor.com/v1/search',
        params=params)

    joke_json = response.json()
    joke_str = joke_json
    return joke_str


if __name__ == "__main__":
    app.run(debug=True, port=8080)
