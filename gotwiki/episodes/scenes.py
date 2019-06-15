from py2neo import Graph
from .utilities import *

class scenesModel:

    def getNumberOfScenesPerCharacter():
        GoT2Neo = getConnection()
        getNumberOfScenesPerCharacterQuery = read_query('gotwiki/episodes/queries/getNumberOfScenesPerCharacter.cyp')
        return {"query": getNumberOfScenesPerCharacterQuery, "data": GoT2Neo.run(getNumberOfScenesPerCharacterQuery)}

    def getTop10LongestScenes():
        GoT2Neo = getConnection()
        getTop10LongestScenesQuery = read_query('gotwiki/episodes/queries/getTop10LongestScenes.cyp')
        return {"query": getTop10LongestScenesQuery, "data": GoT2Neo.run(getTop10LongestScenesQuery)}
