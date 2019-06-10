from . import houses
from flask import render_template

@houses.route('/houses')
def index():
    return render_template('houses/index.html')