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
@episodes.route('/seasons')
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





    return render_template('episodes/visualization.html', result = data)

# Episode: Get duration, given season, of each episode: (episode, toFloat(sum(seconds)) / 3600)
@episodes.route('/episodes_duration')
def episodes_duration():
    season = int(request.args.get('season'))
    result = episodeModel.getDurationEpisodesPerGivenSeason(season)
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)



############# SCENES #############

# Scene:Get number of scenes for each character: (characterName, numberOfScenes)
@episodes.route('/num_scenes_characters')
def num_scenes_characters():
    result = scenesModel.getNumberOfScenesPerCharacter()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Scene: Get top longest scenes: info of the scene and minutes of that
@episodes.route('/longest_scenes')
def longest_scenes():
    result = scenesModel.getTop10LongestScenes()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Scene: Get characters in longest scene for each episode: (episode, collectionCharacters)
@episodes.route('/characters_longest_scene')
def characters_longest_scene():
    result = scenesModel.getCharactersInLongestScenePerEpisode()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Scene: Get longest scenes for each episodes: (episode, time, collectionScenes)
@episodes.route('/longest_scene_episode')
def longest_scene_episode():
    result = scenesModel.getLongestScenePerEpisode()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)



############# MAIN EVENTS #############

##### TODO: Aggiungere morti in numero per ogni stagione 

# Main event: Get deaths for each season: (season number, percentageOfDeaths)
@episodes.route('/deaths_in_seasons')
def deaths_in_seasons():
    result = eventsModel.getDeathPercentagesPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Main event: Get sex scenes number for each season: (season number, sexScenesNumber)
@episodes.route('/sex_count')
def sex_count():
    result = eventsModel.getSexScenesCountPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Main event: Get sex scenes percentage for each season: (season number, sexScenesPercentage)
@episodes.route('/sex_percentage')
def sex_percentage():
    result = eventsModel.getSexScenesPercentagePerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)



############# LOCATIONS #############

# Location: Get location and count where a character belongs to a given a house has killed someone: (location, numbDeaths)
@episodes.route('/kill_house_location')
def kill_house_location():
    house = request.args.get('house')
    result = locationModel.getDeathCountOfHousePerLocation(house)
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Location: Get location and death count of the location : (location, numbDeaths)
@episodes.route('/kill_location_numb')
def kill_location_numb():
    result = locationModel.getDeathCountPerLocation()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Location: Get location and number of scenes set in that location : (location, numbScenes)
@episodes.route('/frequency_locations')
def frequency_locations():
    result = locationModel.getFrequencyPerLocation()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)