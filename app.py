
from flask import Flask, render_template, request
import giphypop
import os

app = Flask(__name__)


# define a function that searches the Giphypop API with the giphypop library
def get_search_function(search_term):
    g = giphypop.Giphy() # giphypop api 
    results = g.search(search_term)
    return results
    
# represents home page
@app.route('/')
def index():
    return render_template('index.html') #points to index.html page

@app.route('/results')
def results():
    gif_search = request.values.get('gif_search')


    if gif_search == "":
        gif_list = []
    else:
        gif_list = get_search_function(gif_search)
#points to the result web-page and send requested information to this page so that it is customized
    return render_template('results.html', gif_search=gif_search, gif_list=gif_list)

  

if __name__ == "__main__":
    app.run(debug=True, port=8080)
