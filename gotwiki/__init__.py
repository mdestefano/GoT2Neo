from flask import Flask
from .houses import houses
from .pages import pages
from .characters import characters
from .episodes import episodes

app = Flask(__name__)

app.register_blueprint(houses,url_prefix="/houses")
app.register_blueprint(pages)
app.register_blueprint(characters, url_prefix="/characters")
app.register_blueprint(episodes, url_prefix="/characters")