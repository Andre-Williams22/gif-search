from flask import Flask, render_template, request
import requests
import json

# TODO: Rename search_term

app = Flask(__name__)


@app.route('/')
def index():

    # userInput = request.form['search_term']
    # processedText = userInput.upper()

    return render_template("index.html")


@app.route('/search', methods=['GET'])
def search():

    search = request.args.get('search_term')
    apiKey = 'MPEYFTLFT9CP'

    response = requests.get(
        f"https://api.tenor.com/v1/search?q={search}&key={apiKey}&limit={10}")

    gif_json = response.json()

    gif_string = gif_json['results']

    return render_template("index.html", gifs=gif_string, search=search)


if __name__ == '__main__':
    app.run(debug=True)
