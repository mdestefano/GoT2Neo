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

    def getCharactersInLongestScenePerEpisode():
        GoT2Neo = getConnection()
        getCharactersInLongestScenePerEpisodeQuery = read_query('gotwiki/episodes/queries/getCharactersInLongestScenePerEpisode.cyp')
        return {"query": getCharactersInLongestScenePerEpisodeQuery, "data": GoT2Neo.run(getCharactersInLongestScenePerEpisodeQuery)}

    def getLongestScenePerEpisode():
        GoT2Neo = getConnection()
        getLongestScenePerEpisodeQuery = read_query('gotwiki/episodes/queries/getLongestScenePerEpisode.cyp')
        return {"query": getLongestScenePerEpisodeQuery, "data": GoT2Neo.run(getLongestScenePerEpisodeQuery)}