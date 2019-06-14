from . import episodes
# TODO change import and make functions statics
from .models import Episodes, getDeathPercentagesPerSeason, getNumberOfScenesPerCharacter, getTop10LongestScenes, getScorePerEpisode, getScoreStatsPerSeason
from flask import render_template

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

# A:Get number of scenes for each character: (characterName, numberOfScenes)
@episodes.route('/num_scenes_characters')
def num_scenes_characters():
    result = getNumberOfScenesPerCharacter()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# A: Get top longest scenes: info of the scene and minutes of that
@episodes.route('/longest_scenes')
def longest_scenes():
    result = getTop10LongestScenes()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# B: Get score for every episodes in order of score Desc: (episodeInfo, meanScore)
@episodes.route('/score_episodes')
def score_episodes():
    result = getScorePerEpisode()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# B: Get mean score and stDev for every season: (season, avgScore, stDevScore)
@episodes.route('/score_season')
def score_season():
    result = getScoreStatsPerSeason()
    data = result["data"]
    query = result["query"]
    return render_template('episodes/index.html', result = data)

# C: Get getTotalDuration of all season: (time)

# C: Get duration of each season: (season, toFloat(sum(seconds)) / 3600)

# C: Get duration, given season, of each episode: (episode, toFloat(sum(seconds)) / 3600)