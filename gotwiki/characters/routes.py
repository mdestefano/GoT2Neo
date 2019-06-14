from gotwiki.characters.models import CharacterManager
from . import characters
from flask import render_template, make_response

index_template = 'characters/index.html'
result_template = 'characters/result.html'


@characters.route('/')
def index():
    return render_template(index_template)


@characters.route('/getCharactersInLongestScenes')
def getCharactersInLongestScenes():
    cm = CharacterManager()
    result = cm.getCharactersInLongestScenes()
    data = result["data"]
    query = result["query"]
    response = make_response(render_template(result_template, data=data, query=query))
    return response


@characters.route('/getDeathCountPerKillCategory')
def getDeathCountPerKillCategory():
    cm = CharacterManager()
    result = cm.getDeathCountPerKillCategory()
    data = result["data"]
    query = result["query"]
    response = make_response(render_template(result_template, data=data, query=query))
    return response

# TODO the other routes
