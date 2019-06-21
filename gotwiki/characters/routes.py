from .models import CharacterManager
from . import characters
from flask import render_template, make_response, escape, request

index_template = 'characters/charactersIndex.html'
longest_scenes_template = 'characters/charactersinlongestscenes.html'
info_template = 'characters/character.html'
relevant_template = 'characters/relevantcharacters.html'
deathcounts_template = 'characters/deathcounts.html'
incests_template = 'characters/incests.html'
killcounts_template = 'characters/killcounts.html'
killmethods_template = 'characters/killmethods.html'
lovers_killers_template = 'characters/loverskillers.html'
relative_killing_template = 'characters/relative_killing.html'
murders_template = 'characters/murders.html'
familytree_template = 'characters/familytree.html'
suicides_template = 'characters/suicides.html'
error_template = 'errorPage.html'


@characters.route('/')
def index():
    return render_template(index_template)


@characters.route('/character')
def getCharacterInfo():
    cm = CharacterManager()
    character_name = request.args.get('name')
    print(character_name)
    if character_name is None:
        return render_template(error_template)
    else:
        result = cm.getCharacterInfo(character_name)
        description = 'About ' + character_name
        query_title = 'getCharacterInfo'
        return __make_response(info_template, result, description, query_title)


@characters.route('/charactersinlongestscenes')
def getCharactersInLongestScenes():
    cm = CharacterManager()
    result = cm.getCharactersInLongestScenes()
    description = 'Characters in longest scenes'
    query_title = 'getCharactersInLongestScenes'
    return __make_response(longest_scenes_template, result, description, query_title)


@characters.route('/deathcounts')
def getDeathCountPerKillCategory():
    cm = CharacterManager()
    result = cm.getDeathCountPerKillCategory()
    description = 'Death count for each kill category'
    query_title = 'getDeathCountPerKillCategory'
    return __make_response(deathcounts_template, result, description, query_title)


@characters.route('/incests')
def getIncests():
    cm = CharacterManager()
    result = cm.getIncests()
    description = 'Incests'
    query_title = 'getIncests'
    return __make_response(incests_template, result, description, query_title)


@characters.route('/killcounts')
def getKillCountPerCharacter():
    cm = CharacterManager()
    result = cm.getKillCountPerCharacter()
    description = 'Kill count for each characters'
    query_title = 'getKillCountPerCharacter'
    return __make_response(killcounts_template, result, description, query_title)


@characters.route('/killmethods')
def getKillMethodsPerCharacter():
    cm = CharacterManager()
    result = cm.getKillMethodsPerCharacter()
    description = 'Kill method for each characters'
    query_title = 'getKillingMethodsPerCharacter'
    return __make_response(killmethods_template, result, description, query_title)


@characters.route('/loverskillers')
def getLoversKillers():
    cm = CharacterManager()
    result = cm.getLoversKillers()
    description = 'Loved but then...'
    query_title = 'getLoversKillers'
    return __make_response(lovers_killers_template, result, description, query_title)


@characters.route('/relativeskillers')
def getMurdersAmongRelatives():
    cm = CharacterManager()
    result = cm.getMurdersAmongRelatives()
    description = 'Relatives that killed each other'
    query_title = 'getMurdersAmongRelatives'
    return __make_response(relative_killing_template, result, description, query_title)


@characters.route('/murdersof/<killer_name>')
def getMurdersByCharacter(killer_name):
    cm = CharacterManager()
    result = cm.getMurdersByCharacter(killer_name)
    description = 'Murders of ' + killer_name
    query_title = 'getMurdersByCharacter'
    return __make_response(murders_template, result, description, query_title)


@characters.route('/familytree/<character_name>')
def getSmallFamilyTree(character_name):
    cm = CharacterManager()
    result = cm.getSmallFamilyTree(character_name)
    description = 'Family Tree of ' + character_name
    query_title = 'getSmallFamilyTree'
    return __make_response(familytree_template, result, description, query_title)


@characters.route('/suicides')
def getSuicides():
    cm = CharacterManager()
    result = cm.getSuicides()
    description = 'Characters who committed suicide'
    query_title = 'getSuicides'
    return __make_response(suicides_template, result, description, query_title)


def __make_response(template, result, description, query_title):
    data = result['data']
    query = result['query']
    if len(data) == 0:
        response = make_response(
            render_template(error_template))
    else:
        response = make_response(
            render_template(template, description=escape(description), data=data, query=escape(query),
                            query_title=escape(query_title)))
    return response
