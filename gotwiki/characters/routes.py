from gotwiki.characters.models import CharacterManager
from . import characters
from flask import render_template, make_response, escape

index_template = 'characters/index.html'
barplot_template = 'characters/barplot.html'
suicides_template = 'characters/suicides.html'
murders_template = 'characters/murders.html'
lovers_killers_template = 'characters/loverskillers.html'


@characters.route('/')
def index():
    return render_template(index_template)


@characters.route('/getDeathCountPerKillCategory')
def getDeathCountPerKillCategory():
    cm = CharacterManager()
    result = cm.getDeathCountPerKillCategory()
    description = 'Death count for each kill category'
    query_title = 'getDeathCountPerKillCategory'
    return __make_response(barplot_template, result, description, query_title)


@characters.route('/getKillCountPerCharacter')
def getKillCountPerCharacter():
    cm = CharacterManager()
    result = cm.getKillCountPerCharacter()
    description = 'Kill count for each characters'
    query_title = 'getKillCountPerCharacter'
    return __make_response(barplot_template, result, description, query_title)


@characters.route('/getLoversKillers')
def getLoversKillers():
    cm = CharacterManager()
    result = cm.getLoversKillers()
    description = 'Loved but then...'
    query_title = 'getLoversKillers'
    return __make_response(lovers_killers_template, result, description, query_title)


@characters.route('/getMurdersByCharacter/<killerName>')
def getMurdersByCharacter(killerName):
    cm = CharacterManager()
    result = cm.getMurdersByCharacter(killerName)
    description = 'Murders of ' + killerName
    query_title = 'getMurdersByCharacter'
    return __make_response(murders_template, result, description, query_title)


@characters.route('/getSuicides')
def getSuicides():
    cm = CharacterManager()
    result = cm.getSuicides()
    description = 'Characters who committed suicide'
    query_title = 'getSuicides'
    return __make_response(suicides_template, result, description, query_title)


def __make_response(template, result, description, query_title):
    data = result['data']
    query = result['query']
    response = make_response(
        render_template(template, description=escape(description), data=data, query=escape(query),
                        query_title=escape(query_title)))
    return response
