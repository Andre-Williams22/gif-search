import requests
from flask import Flask

app = Flask(__name__)





@app.route('/')
def home():
    return "<h1> Hello World </h1>"



if __name__ =="__main__":
    app.run(debug=True,port=8080)
'''
@app.route('/joke')
def make_joke():
    params = { "q": query_term,
    "Key": "1F2TY5LFTDOH" }
    response = requests.get(
    'https://api.tenor.com/v1/search',
    params=params)


    joke_json = response.json()
    joke_str = joke_json
    return joke_str
'''