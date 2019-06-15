from . import *
from .seasons import seasonModel
from .episodesStats import episodeModel
from .scenes import scenesModel
from .mainEvents import eventsModel
from .locations import locationModel

from flask import render_template, request

@episodes.route('/')
def visualization():
    return render_template('episodes/episodesIndex.html')

# Scenes:Get number of scenes for each character: (characterName, numberOfScenes)
@episodes.route('/num_scenes_characters')
def num_scenes_characters():
    result = scenesModel.getNumberOfScenesPerCharacter()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Scenes: Get top longest scenes: info of the scene and minutes of that
@episodes.route('/longest_scenes')
def longest_scenes():
    result = scenesModel.getTop10LongestScenes()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Scores: Get score for every episodes in order of score Desc: (episodeInfo, meanScore)
@episodes.route('/score_episodes')
def score_episodes():
    result = episodeModel.getScorePerEpisode()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Scores: Get mean score and stDev for every season: (season, avgScore, stDevScore)
@episodes.route('/score_season')
def score_season():
    result = seasonModel.getScoreStatsPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# TODO: Aggiungere morti in numero per ogni stagione 
# Main events: Get deaths for each season: (season number, percentageOfDeaths)
@episodes.route('/deaths_in_seasons')
def deaths_in_seasons():
    result = eventsModel.getDeathPercentagesPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Main events: Get sex scenes number for each season: (season number, sexScenesNumber)
@episodes.route('/sex_count')
def sex_count():
    result = eventsModel.getSexScenesCountPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Main events: Get sex scenes percentage for each season: (season number, sexScenesPercentage)
@episodes.route('/sex_percentage')
def sex_percentage():
    result = eventsModel.getSexScenesPercentagePerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Episodes facts: Get stats on viewers: (season, numberViewers, mean, std)
@episodes.route('/viewer_stats')
def viewer_stats():
    result = seasonModel.getViewersStatsPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Episodes facts: Get getTotalDuration of all season: (time)
@episodes.route('/total_duration')
def total_duration():
    result = seasonModel.getTotalDuration()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Episodes facts: Get duration of each season: (season, toFloat(sum(seconds)) / 3600)
@episodes.route('/season_duration')
def season_duration():
    result = seasonModel.getDurationPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Episodes facts: Get duration, given season, of each episode: (episode, toFloat(sum(seconds)) / 3600)
#http://localhost:5000/episodes/episodes_duration?season=1
@episodes.route('/episodes_duration')
def episodes_duration():
    season = int(request.args.get('season'))
    result = episodeModel.getDurationEpisodesPerGivenSeason(season)
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Locations: Get location and count where a character belongs to a given a house has killed someone: (location, numbDeaths)
@episodes.route('/kill_house_location')
def kill_house_location():
    house = request.args.get('house')
    result = locationModel.getDeathCountOfHousePerLocation(house)
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Locations: Get location and death count of the location : (location, numbDeaths)
@episodes.route('/kill_location_numb')
def kill_location_numb():
    result = locationModel.getDeathCountPerLocation()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)

# Locations: Get location and number of scenes set in that location : (location, numbScenes)
@episodes.route('/frequency_locations')
def frequency_locations():
    result = locationModel.getFrequencyPerLocation()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/visualization.html', result = data)