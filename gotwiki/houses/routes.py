from . import houses
from flask import render_template,escape
from .models import HouseModel,House
import plotly
import json

@houses.route('/')
def index():
    return render_template('houses/index.html')

@houses.route('/<houseName>')
def view_house(houseName):
    model = HouseModel(houseName)
    house = model.getHouse()
    pie = {
            'alive':house.alive_c_no,
            'dead':house.dead_c_no
        }
            
    graphJSON = json.dumps(pie)
    return render_template('houses/single.html',house=house,graphJSON=escape(graphJSON))
