from flask import Flask
from flask.logging import create_logger
import logging
import requests
from bs4 import BeautifulSoup
import bs4

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

# @app.route("/")
# def home():
#     html = f"<h3> Merchant of Venice Webreader (Steven Herrera) </h3>"
#     return html.format(format)


@app.route("/")
def test_read():
    """Reads the Merchant of Venice"""
    URL = "http://shakespeare.mit.edu/merchant/full.html"
    response = requests.get(URL, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    assert type(soup.get_text()) == str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
