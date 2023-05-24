from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/")
def read():
    """Reads the Merchant of Venice"""
    URL = "http://shakespeare.mit.edu/merchant/full.html"
    response = requests.get(URL, timeout=10)
    soup = BeautifulSoup(response.content, "html")
    return soup.prettify()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
