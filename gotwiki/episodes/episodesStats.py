from py2neo import Graph
from .utilities import *

class episodeModel:
    def getScorePerEpisode():
        GoT2Neo = getConnection()
        getScorePerEpisodeQuery = read_query('gotwiki/episodes/queries/getScorePerEpisode.cyp')
        return {"query": getScorePerEpisodeQuery, "data": GoT2Neo.run(getScorePerEpisodeQuery)}

    def getDurationOfEachEpisode():
        GoT2Neo = getConnection()
        getDurationOfEachEpisodeQuery = read_query('gotwiki/episodes/queries/getDurationOfEachEpisode.cyp')
        return {"query": getDurationOfEachEpisodeQuery, "data": GoT2Neo.run(getDurationOfEachEpisodeQuery)}

    def getAllEpisodes():
        GoT2Neo = getConnection()
        getAllEpisodesQuery = "MATCH (episode:Episode) RETURN episode ORDER BY episode.episodeGlobal"
        return {"data": GoT2Neo.run(getAllEpisodesQuery)}
