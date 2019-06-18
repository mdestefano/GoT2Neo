from . import houses
from flask import render_template,escape
from .models import HouseModel,House
import plotly
import plotly.graph_objs as go
import json

@houses.route('/')
def index():
    kill_counts_df = HouseModel.get_kill_count_per_houses()

    barchart = [go.Bar(y = kill_counts_df['house'].tolist(),x = kill_counts_df['kills'].tolist(),orientation='h')]
    
    barchart  = json.dumps(barchart, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('houses/index.html',kill_counts_df=kill_counts_df, barchart=barchart)

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
