from . import *
from pandas import DataFrame
from .seasons import seasonModel
from .episodesStats import episodeModel
from .scenes import scenesModel
from .mainEvents import eventsModel
from .locations import locationModel
from flask import render_template, request
from .utilities import getUIParameter
import plotly
import plotly.graph_objs as go
import json

# Route for episode index where user can choose the section of interest
@episodes.route('/')
def visualization():
    return render_template('episodes/episodesIndex.html')



############# SEASONS #############
##ROUTE
@episodes.route('/seasons')
def seasons():
    result = seasonModel.getScoreStatsPerSeason()
    data = result["data"]
    query = result["query"]
    
    scoresDataframe = DataFrame(data)
    season = scoresDataframe[0].tolist()
    mean = scoresDataframe[1].tolist()
    std = scoresDataframe[2].tolist()

    dataMean = getUIParameter(season, mean)
    dataStd = getUIParameter(season, std)

    return render_template('episodes/seasons.html', dataMean = dataMean, dataStd = dataStd, query = query)

# Season: Get duration of each season: (season, toFloat(sum(seconds)) / 3600)
@episodes.route('/season_duration')
def season_duration():
    result = seasonModel.getDurationPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/seasons.html', result = data)

# Season: Get mean score and stDev for every season: (season, avgScore, stDevScore)
@episodes.route('/score_season')
def score_season():
    result = seasonModel.getScoreStatsPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/seasons.html', result = data)

# Season: Get stats on viewers: (season, numberViewers, mean, std)
@episodes.route('/viewer_stats')
def viewer_stats():
    result = seasonModel.getViewersStatsPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/seasons.html', result = data)

# Season: Get getTotalDuration of all season: (time)
@episodes.route('/total_duration')
def total_duration():
    result = seasonModel.getTotalDuration()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/seasons.html', result = data)



############# EPISODES #############

# Episode: Get score for every episodes in order of score Desc: (episodeInfo, meanScore)
@episodes.route('/score_episodes')
def score_episodes():
    result = episodeModel.getScorePerEpisode()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Episode: Get duration, given season, of each episode: (episode, toFloat(sum(seconds)) / 3600)
#http://localhost:5000/episodes/episodes_duration?season=1
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