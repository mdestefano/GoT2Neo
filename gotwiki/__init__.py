from flask import Flask
from .houses import houses

app = Flask(__name__)

app.register_blueprint(houses)