from py2neo import Graph,Node,Entity,Relationship, NodeMatcher, RelationshipMatcher
import pandas as pd

#url = 'bolt://localhost:7687'
url = 'http://localhost:7474'
username = 'GoT2Neo'
password = 'GoT2Neo'
graph = Graph(url + '/db/data/', auth=(username,password))

class House:
    def __init__(self, name,region,seat,words,coa,is_alive,alive_characters,dead_characters,religion,lord):
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
        self.lord = lord.strip()

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
        RETURN c.name as name
        '''
        
        alive_members = graph.run(alive_characters_query,alive=True,name=self.name).data()
        alive_members = [d['name'] for d in alive_members]

        dead_members = graph.run(alive_characters_query,alive=False,name=self.name).data()
        dead_members = [d['name'] for d in dead_members]

        house = House(houseNode["name"],houseNode["region"],houseNode["seat"],houseNode["words"],houseNode["coa"],
                        houseNode["is_alive"],alive_members,dead_members,houseNode["religion"],houseNode["lord"])
        
        query_list = [
                    {'name': 'getAliveCharacters', 'value':alive_characters_query.format(alive='true',name=self.name)}, 
                    {'name': 'getDeadCharacters', 'value':alive_characters_query.format(alive='false',name=self.name)}
                    ]

        return {'data':house, 'queries': query_list}

    @classmethod
    def get_all(self):
        house_query = "MATCH (h:House) return h.name as name"        
        house_names = graph.run(house_query).to_data_frame()
        house_names = house_names['name'].tolist()
        return house_names

    @classmethod
    def get_kill_count_per_houses(self):
        
        kill_count_query = '''
                            MATCH (h:House)<-[:BELONGS_TO]-(c:Character), (c)-[r:KILLED]->()
                            WITH h, count(r) AS kills
                            RETURN h.name as house, kills
                            ORDER BY kills DESC
                            '''
        query_list = [{'name':'killCount','value':kill_count_query}]

        return {'data': graph.run(kill_count_query).to_data_frame(), 'queries':query_list}
    
    @classmethod
    def get_kills_between(self,house1,house2):
        kills_between_query = '''
                            MATCH
                            (c1:Character)-[b1:BELONGS_TO]->(h1:House),
                            (c2:Character)-[b2:BELONGS_TO]->(h2:House), 
                            (c1)-[k:KILLED]-(c2)
                            WHERE h1.name = {house1} AND h2.name = {house2}
                            RETURN (startNode(k).name) as killer, (endNode(k).name) as killed  
        '''
        query_list = [
                        {'name':'killsBetweenHouses','value':kills_between_query.format(house1=house1,house2=house2)}
                    ]
        return {'data':graph.run(kills_between_query, house1=house1, house2=house2).to_data_frame(),'queries':query_list}

    @classmethod
    def get_sex_between(self,house1,house2):
        sex_between_query = '''
                            MATCH
                            (c1:Character)-[b1:BELONGS_TO]->(h1:House),
                            (c2:Character)-[b2:BELONGS_TO]->(h2:House),
                            (c1)<-[i1:INVOLVES]-(e:Event)-[i2:INVOLVES]->(c2)
                            WHERE h1.name = {house1} AND h2.name = {house2} AND e.kind = 'sex'
                            RETURN c1.name as character_1, c2.name as character_2  
        '''
        query_list = [{'name':'sexBetweenHouses','value':sex_between_query.format(house1=house1,house2=house2)}]
        return {'data':graph.run(sex_between_query, house1=house1, house2=house2).to_data_frame(),'queries':query_list}



def test_connection():
    print(graph)
    matcher = NodeMatcher(graph)
    print(matcher.match("House",name="Baratheon").first())


if __name__ == "__main__":
    test_connection()