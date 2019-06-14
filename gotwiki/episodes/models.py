from py2neo import Graph
import os

# Set connection variables
GoT2NeoUsername = GoT2NeoPassword = 'GoT2Neo'
GoT2NeoUrl = os.environ.get('GoT2NeoUrl',"http://localhost:7474/db/data/")
# Connect to local instance of the graph
GoT2Neo = Graph(GoT2NeoUrl, username = GoT2NeoUsername, password = GoT2NeoPassword)

class Episodes:
    def __init__(self, title):
        self.title = title

def getDeathPercentagesPerSeason():
    getDeathPercentagesPerSeasonQuery = __read_query('gotwiki/episodes/queries/getDeathPercentagesPerSeason.cyp')
    return {"query": getDeathPercentagesPerSeasonQuery, "data": GoT2Neo.run(getDeathPercentagesPerSeasonQuery)}

def getNumberOfScenesPerCharacter():
    getNumberOfScenesPerCharacterQuery = __read_query('gotwiki/episodes/queries/getNumberOfScenesPerCharacter.cyp')
    return {"query": getNumberOfScenesPerCharacterQuery, "data": GoT2Neo.run(getNumberOfScenesPerCharacterQuery)}

def getTop10LongestScenes():
    getTop10LongestScenesQuery = __read_query('gotwiki/episodes/queries/getTop10LongestScenes.cyp')
    return {"query": getTop10LongestScenesQuery, "data": GoT2Neo.run(getTop10LongestScenesQuery)}

def getScorePerEpisode():
    getScorePerEpisodeQuery = __read_query('gotwiki/episodes/queries/getScorePerEpisode.cyp')
    return {"query": getScorePerEpisodeQuery, "data": GoT2Neo.run(getScorePerEpisodeQuery)}

def getScoreStatsPerSeason():
    getScoreStatsPerSeasonQuery = __read_query('gotwiki/episodes/queries/getScoreStatsPerSeason.cyp')
    return {"query": getScoreStatsPerSeasonQuery, "data": GoT2Neo.run(getScoreStatsPerSeasonQuery)}

def getTotalDuration():
    getTotalDurationQuery = __read_query('gotwiki/episodes/queries/getTotalDuration.cyp')
    return {"query": getTotalDurationQuery, "data": GoT2Neo.run(getTotalDurationQuery)}

def getDurationPerSeason():
    getDurationPerSeasonQuery = __read_query('gotwiki/episodes/queries/getDurationPerSeason.cyp')
    return {"query": getDurationPerSeasonQuery, "data": GoT2Neo.run(getDurationPerSeasonQuery)}

def getDurationEpisodesPerGivenSeason(season):
    getDurationEpisodesPerGivenSeasonQuery = __read_query('gotwiki/episodes/queries/getDurationEpisodesPerGivenSeason.cyp')
    return {"query": getDurationEpisodesPerGivenSeasonQuery, "data": GoT2Neo.run(getDurationEpisodesPerGivenSeasonQuery,season = season)}

def __read_query(query_path):
    with open(query_path, 'r') as file:
        query = file.read().replace('\n', ' ')
    return query