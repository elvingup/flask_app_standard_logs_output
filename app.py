
from flask import Flask
import logging
import sys

app = Flask(__name__)

# Configure logging to output to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@app.route("/")
def hello():
    app.logger.info("Accessed '/' route")
    return "Hello, World!"


@app.route("/about")
def about():
	app.logger.info("Accessed '/about' route")
    return "Ola, voce acessou a pagina sobre: <br> Eu sou o dev <br> "


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
