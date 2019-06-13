from . import houses
from flask import render_template,jsonify
from .models import HouseModel,House

@houses.route('/')
def index():
    return render_template('houses/index.html')

@houses.route('/<houseName>')
def view_house(houseName):
    model = HouseModel(houseName)
    house = model.getHouse()
    return house.__str__()
