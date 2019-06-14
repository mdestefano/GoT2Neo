from flask import json
from py2neo import Graph


class Character:
    def __init__(self, name, actor, house, image_full, image_thumb, is_royal, nickname):
        self.name = name
        self.actor = actor
        self.house = house
        self.imageFull = image_full
        self.imageThumb = image_thumb
        self.isRoyal = is_royal
        self.nickname = nickname


class CharacterManager:
    def __init__(self):
        self.__url = 'bolt://localhost:7687'
        self.__username = 'GoT2Neo'
        self.__password = 'GoT2Neo'
        self.graph = Graph(self.__url, user=self.__username, password=self.__password)

    def getDeathCountPerKillCategory(self):
        query = self.__read_query('gotwiki/characters/queries/getDeathCountPerKillCategory.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        data_json = json.dumps(data)
        return {"query": query, "data": data_json}

    def getKillCountPerCharacter(self):
        query = self.__read_query('gotwiki/characters/queries/getKillCountPerCharacter.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        data_json = json.dumps(data)
        return {"query": query, "data": data_json}

    def getMurdersByCharacter(self, killerName):
        query = self.__read_query('gotwiki/characters/queries/getMurdersByCharacter.cyp')
        cursor = self.graph.run(query, characterName=killerName)
        data = cursor.data()
        data_json = json.dumps(data)
        return {"query": query, "data": data_json}

    def getSuicides(self):
        query = self.__read_query('gotwiki/characters/queries/getSuicides.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        data_json = json.dumps(data)
        return {"query": query, "data": data_json}

    @staticmethod
    def __read_query(query_path):
        with open(query_path, 'r') as file:
            query = file.read().replace('\n', ' ')
        return query

# Plot setup
# bars = [method_cat['k.methodCat'] for method_cat in data]
# length = np.arange(len(bars))
# counts = [method_cat['count(k.methodCat)'] for method_cat in data]
# pyplot.bar(length, counts)
# pyplot.xticks(length, bars)
# pyplot.show()
