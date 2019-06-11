from . import pages
from flask import render_template

@pages.route('/')
def index():
    return render_template('pages/index.html')