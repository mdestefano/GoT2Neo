from py2neo import Graph
from .utilities import *

class locationModel:
    def getDeathCountOfHousePerLocation(house):
        GoT2Neo = getConnection()
        getDeathCountOfHousePerLocationQuery = read_query('gotwiki/episodes/queries/getDeathCountOfHousePerLocation.cyp')
        return {"query": getDeathCountOfHousePerLocationQuery, "data": GoT2Neo.run(getDeathCountOfHousePerLocationQuery, house_var = house)}

    def getDeathCountPerLocation():
        GoT2Neo = getConnection()
        getDeathCountPerLocationQuery = read_query('gotwiki/episodes/queries/getDeathCountPerLocation.cyp')
        return {"query": getDeathCountPerLocationQuery, "data": GoT2Neo.run(getDeathCountPerLocationQuery)}

    def getFrequencyPerLocation():
        GoT2Neo = getConnection()
        getFrequencyPerLocationQuery = read_query('gotwiki/episodes/queries/getFrequencyPerLocation.cyp')
        return {"query": getFrequencyPerLocationQuery, "data": GoT2Neo.run(getFrequencyPerLocationQuery)}
