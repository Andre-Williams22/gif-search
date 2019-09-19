# Gif Search

![Gif Site](https://i.imgur.com/eXxSJXg.png)

## About
This Gif search project displays randomized gifs from tenors API on the home page in columns. The max number of gifs displayed on the page is 10. If the user wants to see a specific category of gifs they have the autonomy to use the search bar and look for certain gifs. There are also the top ten trending, entertaining, sports, and programming categories that display the top ten trending gifs at the moment through different web pages with jinja templates. Ultimately, the gif search provides unlimited access to gifs with tenor's API, flask, and jinja templates.

## Authors

* **Andre Williams and Alex Barksdale** - [Alex's GitHub](https://github.com/alexbarksdale)
* Check Alex's branch for most of his work and master branch

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
If you haven't already installed pip3 for Python3
```
sudo apt install python3-pip
```
Install flask and requests
```
pip3 install flask
pip3 install requests
```

### Installing

1. Clone the respository
```
git clone https://github.com/Andre-Williams22/gif-search.git
```
2. Make sure in the correct directory

3. Enter the development environment
```
export FLASK_ENV=development 
```
4. Open your terminal and run flask
```
flask run
```
You should see something similar to the output below:
```
* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
* Debug mode: off
* Running on (Your Localhost IP) (Press CTRL+C to quit)
```
## Running the tests
(TODO)

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - Lightweight web application framework
* [Jinja](https://palletsprojects.com/p/jinja/) - Template engine for python
* [Tenor API](https://tenor.com/gifapi) - Used Tenor's API for Gifs

## Acknowledgments

* Used Make School's starter code to get started: [Make School's Repo](https://github.com/Make-School-Labs/Gif-Search-Starter)

