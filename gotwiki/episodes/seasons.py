from py2neo import Graph
from .utilities import *

class seasonModel:
    def getDurationPerSeason():
        GoT2Neo = getConnection()
        getDurationPerSeasonQuery = read_query('gotwiki/episodes/queries/getDurationPerSeason.cyp')
        return {"query": getDurationPerSeasonQuery, "data": GoT2Neo.run(getDurationPerSeasonQuery)}

    def getScoreStatsPerSeason():
        GoT2Neo = getConnection()
        getScoreStatsPerSeasonQuery = read_query('gotwiki/episodes/queries/getScoreStatsPerSeason.cyp')
        return {"query": getScoreStatsPerSeasonQuery, "data": GoT2Neo.run(getScoreStatsPerSeasonQuery)}

    def getViewersStatsPerSeason():
        GoT2Neo = getConnection()
        getViewersStatsPerSeasonQuery = read_query('gotwiki/episodes/queries/getViewersStatsPerSeason.cyp')
        return {"query": getViewersStatsPerSeasonQuery, "data": GoT2Neo.run(getViewersStatsPerSeasonQuery)}
    
    def getTotalDuration():
        GoT2Neo = getConnection()
        getTotalDurationQuery = read_query('gotwiki/episodes/queries/getTotalDuration.cyp')
        return {"query": getTotalDurationQuery, "data": GoT2Neo.run(getTotalDurationQuery)}