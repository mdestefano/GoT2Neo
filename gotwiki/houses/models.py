from py2neo import Graph,Node,Entity,Relationship, NodeMatcher

#url = 'bolt://localhost:7687'
url = 'http://localhost:7474'
username = 'Got2Neo'
password = 'Got2Neo'
graph = Graph(url + '/db/data/', auth=(username,password))

def test_connection():
    print(graph)
    matcher = NodeMatcher(graph)
    print(matcher.match("House",name="Baratheon").first())


if __name__ == "__main__":
    test_connection()