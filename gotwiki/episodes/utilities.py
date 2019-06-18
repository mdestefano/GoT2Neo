from py2neo import Graph
import os
import plotly
import plotly.graph_objs as go
import json

# Reading query file
def read_query(query_path):
    with open(query_path, 'r') as file:
        query = file.read()
    return query

# Get connection for GoT2Neo database
def getConnection():
    GoT2NeoUrl = os.environ.get('GoT2NeoUrl',"http://localhost:7474/db/data/")
    GoT2NeoUsername = 'GoT2Neo'
    GoT2NeoPassword = 'GoT2Neo'
    return Graph(GoT2NeoUrl, username = GoT2NeoUsername, password = GoT2NeoPassword)

# Get Json for couple paramter in the page
def encodeCoupleParameter(xValue, yValue):
    data = [
        go.Bar(
            x = xValue,
            y = yValue
        )
    ]
    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

# Get Json for single paramter of UI
def encodeSingleParameter(xValue):
    data = [go.Bar(x = xValue)]

    return json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

# Create list for property
def getListForProperty(nodeRecords, propertyName):
    paramList = list()

    for node in nodeRecords:
        paramList.append(node[propertyName])

    return paramList