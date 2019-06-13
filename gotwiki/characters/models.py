import numpy as np
import matplotlib.pyplot as pyplot
from py2neo import Graph


class CharacterManager:
    def __init__(self):
        self.__url = 'bolt://localhost:7687'
        self.__username = 'GoT2Neo'
        self.__password = 'GoT2Neo'
        self.graph = Graph(self.__url, user=self.__username, password=self.__password)

    def getCharactersInLongestScenes(self):
        query = self.__read_query('gotwiki/characters/queries/getCharactersInLongestScenes.cyp')
        cursor = self.graph.run(query)
        return {"query": query, "data": cursor.data()}

    def getDeathCountPerKillCategory(self):
        query = self.__read_query('gotwiki/characters/queries/getDeathCountPerKillCategory.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()

        # Plot setup
        # TODO fix and return png image instead of textual data
        bars = [method_cat['k.methodCat'] for method_cat in data]
        length = np.arange(len(bars))
        counts = [method_cat['count(k.methodCat)'] for method_cat in data]
        pyplot.bar(length, counts)
        pyplot.xticks(length, bars)
        pyplot.show()
        return {"query": query, "data": data}

    def getIncests(self):
        query = self.__read_query('gotwiki/characters/queries/getIncests.cyp')
        cursor = self.graph.run(query)
        return {"query": query, "data": cursor.data()}

    def getKillCountPerCharacter(self):
        query = self.__read_query('gotwiki/characters/queries/getKillCountPerCharacter.cyp')
        cursor = self.graph.run(query)
        return {"query": query, "data": cursor.data()}

    def getLoversKillers(self):
        query = self.__read_query('gotwiki/characters/queries/getLoversKillers.cyp')
        cursor = self.graph.run(query)
        return {"query": query, "data": cursor.data()}

    def getMurdersByCharacter(self, character_name):
        query = self.__read_query('gotwiki/characters/queries/getMurdersByCharacter.cyp')
        cursor = self.graph.run(query, character_name=character_name)
        return {"query": query, "data": cursor.data()}

    def getSmallFamilyTree(self, character_name):
        query = self.__read_query('gotwiki/characters/queries/getSmallFamilyTree.cyp')
        cursor = self.graph.run(query, character_name=character_name)
        return {"query": query, "data": cursor.data()}

    def getSuicides(self):
        query = self.__read_query('gotwiki/characters/queries/getSuicides.cyp')
        cursor = self.graph.run(query)
        return {"query": query, "data": cursor.data()}

    @staticmethod
    def __read_query(query_path):
        with open(query_path, 'r') as file:
            query = file.read().replace('\n', ' ')
        return query
