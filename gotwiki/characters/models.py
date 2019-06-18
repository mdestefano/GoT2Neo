from flask import json
from py2neo import Graph


class CharacterManager:
    def __init__(self):
        self.__url = 'bolt://localhost:7687'
        self.__username = 'GoT2Neo'
        self.__password = 'GoT2Neo'
        self.graph = Graph(self.__url, user=self.__username, password=self.__password)

    def getCharacterInfo(self, characterName):
        query = self.__read_query('gotwiki/characters/queries/getCharacterInfo.cyp')
        cursor = self.graph.run(query, characterName=characterName)
        data = cursor.data()
        return {"query": query, "data": data}

    def getDeathCountPerKillCategory(self):
        query = self.__read_query('gotwiki/characters/queries/getDeathCountPerKillCategory.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        data_json = json.dumps(data)
        return {"query": query, "data": data_json}

    def getIncests(self):
        query = self.__read_query('gotwiki/characters/queries/getIncests.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getKillCountPerCharacter(self):
        query = self.__read_query('gotwiki/characters/queries/getKillCountPerCharacter.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        data_json = json.dumps(data)
        return {"query": query, "data": data_json}

    def getLoversKillers(self):
        query = self.__read_query('gotwiki/characters/queries/getLoversKillers.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getMurdersAmongRelatives(self):
        query = self.__read_query('gotwiki/characters/queries/getMurdersAmongRelatives.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getMurdersByCharacter(self, killerName):
        query = self.__read_query('gotwiki/characters/queries/getMurdersByCharacter.cyp')
        cursor = self.graph.run(query, characterName=killerName)
        data = cursor.data()
        return {"query": query, "data": data}

    def getSuicides(self):
        query = self.__read_query('gotwiki/characters/queries/getSuicides.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

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
