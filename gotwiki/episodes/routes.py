from . import *
from pandas import DataFrame
from .seasons import seasonModel
from .episodesStats import episodeModel
from .scenes import scenesModel
from .mainEvents import eventsModel
from .locations import locationModel
from flask import render_template, request
from .utilities import encodeCoupleParameter, encodeSingleParameter, getListForProperty
import plotly
import plotly.graph_objs as go
import json

# Route for episode index where user can choose the section of interest
@episodes.route('/')
def visualization():
    return render_template('episodes/episodesIndex.html')

# Error page handler with redirection to "episodes" section
@episodes.app_errorhandler(404)
def page_not_found(e):
    return render_template('errorPage.html', page ='/episodes')

############# SEASONS #############
##ROUTE
@episodes.route('/seasonsStats')
def seasons():
    # Season: Get mean score and stDev for every season: (season, avgScore, stDevScore)
    result = seasonModel.getScoreStatsPerSeason()
    data = result["data"]
    query_score = result["query"]
    
    scoresDataframe = DataFrame(data)
    season = scoresDataframe[0].tolist()
    mean = scoresDataframe[1].tolist()
    std = scoresDataframe[2].tolist()

    dataMean = encodeCoupleParameter(season, mean)
    dataStd = encodeCoupleParameter(season, std)

    # Season: Get duration of each season: (season, toFloat(sum(seconds)) / 3600)
    result = seasonModel.getDurationPerSeason()
    data = result["data"]
    query_duration = result["query"]
    
    durationDataframe = DataFrame(data)
    seasonLabels = encodeSingleParameter(durationDataframe[0].tolist())
    seasonDurations = encodeSingleParameter(durationDataframe[1].tolist())

    # Season: Get stats on viewers: (season, numberViewers, mean, std)
    result = seasonModel.getViewersStatsPerSeason()
    data = result["data"]
    query_viewers = result["query"]

    viewersDataframe = DataFrame(data)
    season = viewersDataframe[0].tolist()
    numbViewers = viewersDataframe[1].tolist()
    mean = viewersDataframe[2].tolist()
    std = viewersDataframe[3].tolist()

    numbViewers = encodeCoupleParameter(season, numbViewers)
    meanViewers = encodeCoupleParameter(season, mean)
    stdViewers = encodeCoupleParameter(season, std)

    return render_template('episodes/seasons.html', 
                            dataMean = dataMean, 
                            dataStd = dataStd,
                            seasonLabels = seasonLabels,
                            seasonDurations = seasonDurations,
                            numbViewers = numbViewers,
                            meanViewers = meanViewers,
                            stdViewers = stdViewers,
                            query_score = query_score,
                            query_duration = query_duration,
                            query_viewers = query_viewers
                          )



### useful?
# Season: Get getTotalDuration of all season: (time)
# # # @episodes.route('/total_duration')
# # # def total_duration():
# # #     result = seasonModel.getTotalDuration()
# # #     data = result["data"]
# # #     query = result["query"]
# # #     return render_template('episodes/seasons.html', result = data)


############# EPISODES #############
##ROUTE
@episodes.route('/episodesStats')
def episodesStats():
    #Get all episodes
    result = episodeModel.getAllEpisodes()
    data = result["data"]
    episodesDataframe = DataFrame(data.data())
    episodeNodes = episodesDataframe["episode"]
    
    titleList = getListForProperty(episodeNodes, "title")
    titleList = encodeSingleParameter(titleList)

    seasonList = getListForProperty(episodeNodes, "season")
    seasonList = encodeSingleParameter(seasonList)

    episodeList = getListForProperty(episodeNodes, "episode")
    episodeList = encodeSingleParameter(episodeList)

    episodeGlobalList = getListForProperty(episodeNodes, "episodeGlobal")
    episodeGlobalList = encodeSingleParameter(episodeGlobalList)

    writerList = getListForProperty(episodeNodes, "writer")
    writerList = encodeSingleParameter(writerList)
    
    directorList = getListForProperty(episodeNodes, "director")
    directorList = encodeSingleParameter(directorList)
    
    viewersList = getListForProperty(episodeNodes, "viewers")
    viewersList = encodeSingleParameter(viewersList)

    airDateList = getListForProperty(episodeNodes, "airDate")
    airDateList = encodeSingleParameter(airDateList)

    # Episode: Get score for every episodes in order of score Desc: (episodeInfo, meanScore)
    result = episodeModel.getScorePerEpisode()
    data = result["data"]
    query_episodes_score = result["query"]

    scoresDataframe = DataFrame(data.data())
    episodeNodes = scoresDataframe["episode"]
    
    scoreTitleList = getListForProperty(episodeNodes, "title")
    scoreTitleList = encodeSingleParameter(scoreTitleList)

    scoreSeasonList = getListForProperty(episodeNodes, "season")
    scoreSeasonList = encodeSingleParameter(scoreSeasonList)

    scoreEpisodeList = getListForProperty(episodeNodes, "episode")
    scoreEpisodeList = encodeSingleParameter(scoreEpisodeList)
    
    episodesMeanScores = encodeSingleParameter(scoresDataframe["meanScore"].tolist())

    # Episode: Get duration of each episode: (episodeGlobal, toFloat(sum(seconds)) / 60)
    result = episodeModel.getDurationOfEachEpisode()
    data = result["data"]
    query_episodes_duration = result["query"]
    episodesDurationDataframe = DataFrame(data)

    episodesGlobalNumb = episodesDurationDataframe[0].tolist()
    episodesDuration = episodesDurationDataframe[1].tolist()


    episodesDuration = encodeCoupleParameter(episodesGlobalNumb, episodesDuration)

    return render_template('episodes/episodes_stats.html',
                            titleList = titleList,
                            seasonList = seasonList,
                            episodeList = episodeList,
                            episodeGlobalList = episodeGlobalList,
                            writerList = writerList,
                            directorList = directorList,
                            viewersList = viewersList,
                            airDateList = airDateList,
                            scoreTitleList = scoreTitleList,
                            scoreSeasonList = scoreSeasonList,
                            scoreEpisodeList = scoreEpisodeList,
                            episodesDuration = episodesDuration,
                            episodesMeanScores = episodesMeanScores,
                            query_episodes_score = query_episodes_score,
                            query_episodes_duration = query_episodes_duration
                          )



############# SCENES #############
### Not useful visualizations
# Scene:Get number of scenes for each character: (characterName, numberOfScenes)
# # # # @episodes.route('/num_scenes_characters')
# # # # def num_scenes_characters():
# # # #     result = scenesModel.getNumberOfScenesPerCharacter()
# # # #     data = result["data"]
# # # #     query = result["query"]
# # # #     return render_template('episodes/visualization.html', result = data)

# # # # # Scene: Get top longest scenes: info of the scene and minutes of that
# # # # @episodes.route('/longest_scenes')
# # # # def longest_scenes():
# # # #     result = scenesModel.getTop10LongestScenes()
# # # #     data = result["data"]
# # # #     query = result["query"]
# # # #     return render_template('episodes/visualization.html', result = data)

# # # # # Scene: Get characters in longest scene for each episode: (episode, collectionCharacters)
# # # # @episodes.route('/characters_longest_scene')
# # # # def characters_longest_scene():
# # # #     result = scenesModel.getCharactersInLongestScenePerEpisode()
# # # #     data = result["data"]
# # # #     query = result["query"]
# # # #     return render_template('episodes/visualization.html', result = data)

# # # # # Scene: Get longest scenes for each episodes: (episode, time, collectionScenes)
# # # # @episodes.route('/longest_scene_episode')
# # # # def longest_scene_episode():
# # # #     result = scenesModel.getLongestScenePerEpisode()
# # # #     data = result["data"]
# # # #     query = result["query"]
# # # #     return render_template('episodes/visualization.html', result = data)



############# MAIN EVENTS #############

@episodes.route('/eventsStats')
def events():
    # Main event: Get death number for each season: (season number, deathNumber)  
    result = eventsModel.getDeathNumberPerSeason()
    data = result["data"]
    queryDeathNumber = result["query"]

    deathsNumberDataframe = DataFrame(data)
    deathSeason = deathsNumberDataframe[0].tolist()
    deathNumber = deathsNumberDataframe[1].tolist()

    seasonAndDeathNumber = encodeCoupleParameter(deathSeason, deathNumber)

    deathNumber = encodeSingleParameter(deathNumber)
    deathSeason = encodeSingleParameter(deathSeason)

    # Main event: Get deaths for each season: (season number, percentageOfDeaths)
    result = eventsModel.getDeathPercentagesPerSeason()
    data = result["data"]
    queryDeathPercentage = result["query"]

    deathsPercentageDataframe = DataFrame(data)

    deathSeasonPercentage = deathsNumberDataframe[0].tolist()
    deathPercentage = deathsPercentageDataframe[1].tolist()

    seasonAndDeathPercentage = encodeCoupleParameter(deathSeasonPercentage, deathPercentage)

    # Main event: Get sex scenes number for each season: (season number, sexScenesNumber)
    result = eventsModel.getSexScenesCountPerSeason()
    data = result["data"]
    querySexNumber = result["query"]

    sexNumberDataframe = DataFrame(data)
    sexSeason = sexNumberDataframe[0].tolist()
    sexNumber = sexNumberDataframe[1].tolist()

    seasonAndSexNumber = encodeCoupleParameter(sexSeason, sexNumber)

    sexNumber = encodeSingleParameter(sexNumber)
    sexSeason = encodeSingleParameter(sexSeason)

    # Main event: Get sex scenes percentage for each season: (season number, sexScenesPercentage)
    result = eventsModel.getSexScenesPercentagePerSeason()
    data = result["data"]
    querySexPercentage = result["query"]

    sexPercentageDataframe = DataFrame(data)

    sexSeasonPercentage = sexNumberDataframe[0].tolist()
    sexPercentage = sexPercentageDataframe[1].tolist()

    seasonAndSexPercentage = encodeCoupleParameter(sexSeasonPercentage, sexPercentage)

    return render_template('episodes/events.html',
                            deathNumber = deathNumber,
                            deathSeason = deathSeason,
                            seasonAndDeathNumber = seasonAndDeathNumber,
                            seasonAndDeathPercentage = seasonAndDeathPercentage,
                            sexNumber = sexNumber,
                            sexSeason = sexSeason,
                            seasonAndSexNumber = seasonAndSexNumber,
                            seasonAndSexPercentage = seasonAndSexPercentage,
                            queryDeathNumber = queryDeathNumber,
                            queryDeathPercentage = queryDeathPercentage,
                            querySexNumber = querySexNumber,
                            querySexPercentage = querySexPercentage
                            )

############# LOCATIONS #############

@episodes.route('/locationsStats')
def locations():
    # Location: Get location and death count of the location : (location, numbDeaths)
    result = locationModel.getDeathCountPerLocation()
    data = result["data"]
    queryDeathCountLocation = result["query"]

    locationDeathsDataframe = DataFrame(data)
    locationName = locationDeathsDataframe[0].tolist()
    locationDeaths = locationDeathsDataframe[1].tolist()

    locationAndDeaths = encodeCoupleParameter(locationName, locationDeaths)

    locationName = encodeSingleParameter(locationName)
    locationDeaths = encodeSingleParameter(locationDeaths)

    # Location: Get location and count where characters that belong to a given a house have killed someone: (location, numbDeaths)
    starkHouse = 'Stark'
    result = locationModel.getDeathCountOfHousePerLocation(starkHouse)
    data = result["data"]
    queryStarkTarg = result["query"]

    StarkLocationDeathsDataframe = DataFrame(data)
    StarkLocationName = StarkLocationDeathsDataframe[0].tolist()
    StarkLocationDeaths = StarkLocationDeathsDataframe[1].tolist()

    StarkLocationAndDeaths = encodeCoupleParameter(StarkLocationName, StarkLocationDeaths)

    StarkLocationName = encodeSingleParameter(StarkLocationName)
    StarkLocationDeaths = encodeSingleParameter(StarkLocationDeaths)

    TargaryenHouse = 'Targaryen'
    result = locationModel.getDeathCountOfHousePerLocation(TargaryenHouse)
    data = result["data"]

    TargaryenLocationDeathsDataframe = DataFrame(data)
    TargaryenLocationName = TargaryenLocationDeathsDataframe[0].tolist()
    TargaryenLocationDeaths = TargaryenLocationDeathsDataframe[1].tolist()

    TargaryenLocationAndDeaths = encodeCoupleParameter(TargaryenLocationName, TargaryenLocationDeaths)

    TargaryenLocationName = encodeSingleParameter(TargaryenLocationName)
    TargaryenLocationDeaths = encodeSingleParameter(TargaryenLocationDeaths)

    # Location: Get location and number of scenes set in that location : (location, numbScenes)
    result = locationModel.getFrequencyPerLocation()
    data = result["data"]
    querySceneLocation = result["query"]

    FrequencyLocationDataframe = DataFrame(data)
    FrequencyLocationName = FrequencyLocationDataframe[0].tolist()
    FrequencyLocationNumber = FrequencyLocationDataframe[1].tolist()

    FrequencyLocationAndDeaths = encodeCoupleParameter(FrequencyLocationName, FrequencyLocationNumber)

    FrequencyLocationName = encodeSingleParameter(FrequencyLocationName)
    FrequencyLocationNumber = encodeSingleParameter(FrequencyLocationNumber)

    return render_template('episodes/locations.html',
                            locationAndDeaths = locationAndDeaths,
                            locationName = locationName,
                            locationDeaths = locationDeaths,
                            StarkLocationAndDeaths = StarkLocationAndDeaths,
                            StarkLocationName = StarkLocationName,
                            StarkLocationDeaths = StarkLocationDeaths,
                            TargaryenLocationAndDeaths = TargaryenLocationAndDeaths,
                            TargaryenLocationName = TargaryenLocationName,
                            TargaryenLocationDeaths = TargaryenLocationDeaths,
                            FrequencyLocationAndDeaths = FrequencyLocationAndDeaths,
                            FrequencyLocationName = FrequencyLocationName,
                            FrequencyLocationNumber = FrequencyLocationNumber,
                            queryDeathCountLocation = queryDeathCountLocation,
                            queryStarkTarg = queryStarkTarg,
                            querySceneLocation = querySceneLocation
                            )


