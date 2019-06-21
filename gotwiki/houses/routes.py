from . import houses
from flask import render_template,escape,request
from .models import HouseModel,House
import plotly
import plotly.graph_objs as go
import json


@houses.route('/')
def index():
    house_names = HouseModel.get_all()
    return render_template('houses/index.html',houses=house_names)

@houses.route('/house-kills')
def house_kills():
    result = HouseModel.get_kill_count_per_houses()
    kill_counts_df = result['data']
    queries = result['queries']

    barchart = [go.Bar(y = kill_counts_df['house'].tolist(),x = kill_counts_df['kills'].tolist(),orientation='h')]
    
    barchart  = json.dumps(barchart, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('houses/house_kills.html',kill_counts_df=kill_counts_df, barchart=barchart,queries=queries)

@houses.route('/<houseName>')
def view_house(houseName):
    model = HouseModel(houseName)
    house = model.getHouse()["data"]
    queries = model.getHouse()["queries"]
    pie_values = [{
        'x':[house.alive_c_no,house.dead_c_no]
    }]

    pie_labels = [
        'alive', 'deads'
    ]
            
    pie_labels = json.dumps(pie_labels,cls=plotly.utils.PlotlyJSONEncoder)
    pie_values = json.dumps(pie_values,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('houses/single.html',house=house,pie_labels=pie_labels,pie_values=pie_values ,queries=queries)

@houses.route('/compare',methods=['GET'])
def compare_houses():
    house1 = request.args.get('house1')
    house2 = request.args.get('house2')

    if house1 == house2:
        #flash
        pass
    else:
        house_entity_1 = HouseModel(house1).getHouse()['data']
        house_entity_2 = HouseModel(house2).getHouse()['data']           
        kills_result = HouseModel.get_kills_between(house1,house2)     
        kills_between_df = kills_result['data']    
        sex_result = HouseModel.get_sex_between(house1,house2)
        sex_between_df = sex_result["data"]
        queries = kills_result['queries'] + sex_result["queries"]
        return render_template('houses/compare.html',
                                house_entity_1=house_entity_1,
                                house_entity_2=house_entity_2,
                                kills_between_df=kills_between_df,
                                sex_between_df=sex_between_df,
                                queries=queries
                            )
        