from . import episodes
# TODO change import and make functions statics
from .models import Episodes, getDeathPercentagesPerSeason, getNumberOfScenesPerCharacter, getTop10LongestScenes, getScorePerEpisode, getScoreStatsPerSeason, getTotalDuration, getDurationPerSeason,getDurationEpisodesPerGivenSeason
from flask import render_template, request

@episodes.route('/')
def index():
    return render_template('episodes/index.html', result = "null")

# Get deaths for each season: (season number, percentageOfDeaths)
@episodes.route('/deaths_in_seasons')
def deaths_in_seasons():
    result = getDeathPercentagesPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Scenes:Get number of scenes for each character: (characterName, numberOfScenes)
@episodes.route('/num_scenes_characters')
def num_scenes_characters():
    result = getNumberOfScenesPerCharacter()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Scenes: Get top longest scenes: info of the scene and minutes of that
@episodes.route('/longest_scenes')
def longest_scenes():
    result = getTop10LongestScenes()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Scores: Get score for every episodes in order of score Desc: (episodeInfo, meanScore)
@episodes.route('/score_episodes')
def score_episodes():
    result = getScorePerEpisode()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Scores: Get mean score and stDev for every season: (season, avgScore, stDevScore)
@episodes.route('/score_season')
def score_season():
    result = getScoreStatsPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Episodes_duration: Get getTotalDuration of all season: (time)
@episodes.route('/total_duration')
def total_duration():
    result = getTotalDuration()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Episodes_duration: Get duration of each season: (season, toFloat(sum(seconds)) / 3600)
@episodes.route('/season_duration')
def season_duration():
    result = getDurationPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# Episodes_duration: Get duration, given season, of each episode: (episode, toFloat(sum(seconds)) / 3600)
#http://localhost:5000/episodes/episodes_duration?season=1
@episodes.route('/episodes_duration')
def episodes_duration():
    season = int(request.args.get('season'))
    result = getDurationEpisodesPerGivenSeason(season)
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)