from pandas import DataFrame
from py2neo import Graph

from gotwiki.utilities import encodeCoupleParameter


class CharacterManager:
    def __init__(self):
        self.__url = 'bolt://localhost:7687'
        self.__username = 'GoT2Neo'
        self.__password = 'GoT2Neo'
        self.graph = Graph(self.__url, auth=(self.__username, self.__password))

    def getCharacter(self, characterName):
        query = self.__read_query('gotwiki/characters/queries/getCharacter.cyp')
        cursor = self.graph.run(query, characterName=characterName)
        data = cursor.data()
        return {"query": query, "data": data}

    def getCharactersInLongestScenes(self):
        query = self.__read_query('gotwiki/characters/queries/getCharactersInLongestScenes.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getDeathCountsPerKillCategory(self):
        query = self.__read_query('gotwiki/characters/queries/getDeathCountsPerKillCategory.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        deathcount_df = DataFrame(data)
        method_cats = deathcount_df['methodCat'].tolist()
        counts = deathcount_df['count'].tolist()
        deathcounts = encodeCoupleParameter(method_cats, counts)
        return {"query": query, "data": deathcounts}

    def getIncests(self):
        query = self.__read_query('gotwiki/characters/queries/getIncests.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getKillCountPerCharacter(self):
        query = self.__read_query('gotwiki/characters/queries/getKillCountPerCharacter.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        killcount_df = DataFrame(data)
        characters = killcount_df['character']
        characters_name = [c.get('name') for c in characters]
        counts = killcount_df['count'].tolist()
        killcounts = encodeCoupleParameter(characters_name, counts)
        return {"query": query, "data": killcounts}

    def getKillMethodsPerCharacter(self):
        query = self.__read_query('gotwiki/characters/queries/getKillMethodsPerCharacter.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getLoversKillers(self):
        query = self.__read_query('gotwiki/characters/queries/getLoversKillers.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getMurdersByCharacter(self, killer_name):
        query = self.__read_query('gotwiki/characters/queries/getMurdersByCharacter.cyp')
        cursor = self.graph.run(query, character_name=killer_name)
        data = cursor.data()
        return {"query": query, "data": data}

    def getRelativesKillers(self):
        query = self.__read_query('gotwiki/characters/queries/getRelativesKillers.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    def getSuicides(self):
        query = self.__read_query('gotwiki/characters/queries/getSuicides.cyp')
        cursor = self.graph.run(query)
        data = cursor.data()
        return {"query": query, "data": data}

    # def getSmallFamilyTree(self, character_name):
    #     query = self.__read_query('gotwiki/characters/queries/getSmallFamilyTree.cyp')
    #     cursor = self.graph.run(query, character_name=character_name)
    #     data = cursor.data()
    #     family_tree_df = DataFrame(data)
    #     character = family_tree_df['characters'][0]
    #     parents = family_tree_df['parents'].tolist()
    #     grand_parents = family_tree_df['gparents'].tolist()
    #     print(grand_parents)
    #     return {"query": query, "data": data}

    @staticmethod
    def __read_query(query_path):
        with open(query_path, 'r') as file:
            query = file.read()
        return query
