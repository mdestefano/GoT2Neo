from py2neo import Graph,Node,Entity,Relationship, NodeMatcher, RelationshipMatcher
import pandas as pd

#url = 'bolt://localhost:7687'
url = 'http://localhost:7474'
username = 'GoT2Neo'
password = 'GoT2Neo'
graph = Graph(url + '/db/data/', auth=(username,password))

class House:
    def __init__(self, name,region,seat,words,coa,is_alive,alive_characters,dead_characters,religion):
        self.name = name
        self.region = region
        self.seat = seat
        self.words = words
        self.coa = coa
        self.is_alive = is_alive
        self.alive_characters = alive_characters
        self.alive_c_no = len(self.alive_characters)
        self.dead_characters = dead_characters
        self.dead_c_no = len(self.dead_characters)
        self.religion = religion

    def __str__(self):
        return '''[name={},region={}, seat={}, words={}, coa={}, is_alive={}, religion={}, alive_characters={}, #alive={}, dead_characters={},  
                    #deads={}]
        '''.format(self.name,self.region,self.seat,self.words,self.coa,self.is_alive,self.religion,self.alive_characters,self.alive_c_no,
        self.dead_characters,self.dead_c_no)
    


class HouseModel:

    def __init__(self,houseName):
        self.node_matcher = NodeMatcher(graph)
        self.rel_matcher =  RelationshipMatcher(graph)
        self.name = houseName        
    
    def getHouse(self):
        houseNode = self.node_matcher.match("House",name=self.name).first()
        
        alive_characters_query = '''
        MATCH (c:Character)-[:BELONGS_TO]->(h:House)
        WHERE c.isAlive = {alive} AND h.name = {name}
        RETURN c.name
        '''
        
        alive_members = graph.run(alive_characters_query,alive=True,name=self.name).data()
        
        dead_members = graph.run(alive_characters_query,alive=False,name=self.name).data()

        house = House(houseNode["name"],houseNode["region"],houseNode["seat"],houseNode["words"],houseNode["coa"],
                        houseNode["is_alive"],alive_members,dead_members,houseNode["religion"])
        return house

        

def test_connection():
    print(graph)
    matcher = NodeMatcher(graph)
    print(matcher.match("House",name="Baratheon").first())


if __name__ == "__main__":
    test_connection()