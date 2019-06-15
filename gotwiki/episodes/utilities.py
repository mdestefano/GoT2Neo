import os
from py2neo import Graph

# Reading query file
def read_query(query_path):
    with open(query_path, 'r') as file:
        query = file.read().replace('\n', ' ')
    return query

# Get connection for GoT2Neo database
def getConnection():
    GoT2NeoUrl = os.environ.get('GoT2NeoUrl',"http://localhost:7474/db/data/")
    GoT2NeoUsername = 'GoT2Neo'
    GoT2NeoPassword = 'GoT2Neo'
    return Graph(GoT2NeoUrl, username = GoT2NeoUsername, password = GoT2NeoPassword)