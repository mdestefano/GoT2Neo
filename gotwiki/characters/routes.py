from . import characters
from flask import render_template

@characters.route('/')
def index():
    return render_template('characters/index.html')