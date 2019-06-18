from py2neo import Graph
from .utilities import *

class eventsModel:
    def getDeathPercentagesPerSeason():
        GoT2Neo = getConnection()
        getDeathPercentagesPerSeasonQuery = read_query('gotwiki/episodes/queries/getDeathPercentagesPerSeason.cyp')
        return {"query": getDeathPercentagesPerSeasonQuery, "data": GoT2Neo.run(getDeathPercentagesPerSeasonQuery)}
    
    def getDeathNumberPerSeason():
        GoT2Neo = getConnection()
        getDeathNumberPerSeasonQuery = read_query('gotwiki/episodes/queries/getDeathNumberPerSeason.cyp')
        return {"query": getDeathNumberPerSeasonQuery, "data": GoT2Neo.run(getDeathNumberPerSeasonQuery)}
    
    def getSexScenesCountPerSeason():
        GoT2Neo = getConnection()
        getSexScenesCountPerSeasonQuery = read_query('gotwiki/episodes/queries/getSexScenesCountPerSeason.cyp')
        return {"query": getSexScenesCountPerSeasonQuery, "data": GoT2Neo.run(getSexScenesCountPerSeasonQuery)}

    def getSexScenesPercentagePerSeason():
        GoT2Neo = getConnection()
        getSexScenesPercentagePerSeasonQuery = read_query('gotwiki/episodes/queries/getSexScenesPercentagePerSeason.cyp')
        return {"query": getSexScenesPercentagePerSeasonQuery, "data": GoT2Neo.run(getSexScenesPercentagePerSeasonQuery)}