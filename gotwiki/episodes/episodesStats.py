from py2neo import Graph
from .utilities import *

class episodeModel:
    def getScorePerEpisode():
        GoT2Neo = getConnection()
        getScorePerEpisodeQuery = read_query('gotwiki/episodes/queries/getScorePerEpisode.cyp')
        return {"query": getScorePerEpisodeQuery, "data": GoT2Neo.run(getScorePerEpisodeQuery)}

    def getDurationEpisodesPerGivenSeason(season):
        GoT2Neo = getConnection()
        getDurationEpisodesPerGivenSeasonQuery = read_query('gotwiki/episodes/queries/getDurationEpisodesPerGivenSeason.cyp')
        return {"query": getDurationEpisodesPerGivenSeasonQuery, "data": GoT2Neo.run(getDurationEpisodesPerGivenSeasonQuery,season = season)}
