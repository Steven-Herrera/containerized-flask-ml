from flask import Flask, request
from flask.logging import create_logger
import logging
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# @app.route("/")
# def home():
#     html = f"<h3> Merchant of Venice Webreader (Steven Herrera) </h3>"
#     return html.format(format)
    
@app.route("/")
def read():
    """Reads the Merchant of Venice"""
    URL = 'http://shakespeare.mit.edu/merchant/full.html'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html')
    return soup.prettify()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)