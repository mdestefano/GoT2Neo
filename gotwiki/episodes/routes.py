from . import episodes
from flask import render_template

@episodes.route('/')
def index():
    return render_template('episodes/index.html')