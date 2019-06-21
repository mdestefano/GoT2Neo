import os
import urllib.request
import json
from py2neo import Graph

# Set connection variables
GoT2NeoUsername = GoT2NeoPassword = 'GoT2Neo'
GoT2NeoUrl = os.environ.get('GoT2NeoUrl', "http://localhost:7474/db/data/")
# Connect to local instance of the graph
GoT2Neo = Graph(GoT2NeoUrl, auth=(GoT2NeoUsername, GoT2NeoPassword))

# Clean the graph
GoT2Neo.delete_all()

# Index on node with label 'Characters' on property 'name'
GoT2Neo.schema.create_index('Character', 'name')
GoT2Neo.schema.create_index('House', 'name')
GoT2Neo.schema.create_index('Episode', 'season')
GoT2Neo.schema.create_index('Scene', 'season')

# Get file characters.json
charactersJsonUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/characters.json'
with urllib.request.urlopen(charactersJsonUrl) as url:
    charactersJson = json.loads(url.read().decode())

# Insert "Character" nodes
charactersInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/characters/characters.cyp'
with urllib.request.urlopen(charactersInsertUrl) as url:
    charactersInsert = url.read().decode()
GoT2Neo.run(charactersInsert, data=charactersJson)

# Insert of "SIBLING_OF" relations between characters
siblingOfInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/characters/siblingof.cyp'
with urllib.request.urlopen(siblingOfInsertUrl) as url:
    siblingOfInsert = url.read().decode()

GoT2Neo.run(siblingOfInsert, data=charactersJson)

# Insert of "SON_OF" relations between characters
sonOfInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/characters/sonof.cyp'
with urllib.request.urlopen(sonOfInsertUrl) as url:
    sonOfInsert = url.read().decode()

GoT2Neo.run(sonOfInsert, data=charactersJson)

# Insert of "ENGAGED" relations between characters
engagedOfInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/characters/engaged.cyp'
with urllib.request.urlopen(engagedOfInsertUrl) as url:
    engagedOfInsert = url.read().decode()

GoT2Neo.run(engagedOfInsert, data=charactersJson)

# Insert of "KILLED" relations between characters
killedInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/characters/killed.cyp'
with urllib.request.urlopen(killedInsertUrl) as url:
    killedInsert = url.read().decode()

GoT2Neo.run(killedInsert)

# Insert of "house" nodes
housesInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/houses/houses.cyp'
with urllib.request.urlopen(housesInsertUrl) as url:
    housesInsert = url.read().decode()

GoT2Neo.run(housesInsert)

# Insert of "BELONGS_TO" relations between characters and house
houseAffiliationUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/houses/belongsto.cyp'
with urllib.request.urlopen(houseAffiliationUrl) as url:
    houseAffiliation = url.read().decode()

GoT2Neo.run(houseAffiliation, data=charactersJson)

# Insert of "Episodes" nodes
episodesInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/episodes_scenes/episodes.cyp'
with urllib.request.urlopen(episodesInsertUrl) as url:
    episodesInsert = url.read().decode()

GoT2Neo.run(episodesInsert)

# Insert of "Scene" nodes
scenesInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/episodes_scenes/scenes.cyp'
with urllib.request.urlopen(scenesInsertUrl) as url:
    scenesInsert = url.read().decode()

GoT2Neo.run(scenesInsert)

# Insert of "BELONGS_TO" relations between scene and episode
sceneInEpisodeInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/episodes_scenes/scene_belongsto.cyp'
with urllib.request.urlopen(sceneInEpisodeInsertUrl) as url:
    sceneInEpisodeInsert = url.read().decode()

GoT2Neo.run(sceneInEpisodeInsert)

# Insert of "APPEARS_IN" relations between characters and scene
sceneAppearanceInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/episodes_scenes/appearsin.cyp'
with urllib.request.urlopen(sceneAppearanceInsertUrl) as url:
    sceneAppearanceInsert = url.read().decode()

GoT2Neo.run(sceneAppearanceInsert)

# Insert of "Location" nodes
locationInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/location/location.cyp'
with urllib.request.urlopen(locationInsertUrl) as url:
    locationInsert = url.read().decode()

GoT2Neo.run(locationInsert)

# Insert of "SET_IN" relations between location and scene
locationOfScenesInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/location/setin.cyp'
with urllib.request.urlopen(locationOfScenesInsertUrl) as url:
    locationOfScenesInsert = url.read().decode()

GoT2Neo.run(locationOfScenesInsert)

# Insert of "Event" nodes
eventInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/events/sexes.cyp'
with urllib.request.urlopen(eventInsertUrl) as url:
    eventInsert = url.read().decode()

GoT2Neo.run(eventInsert)

# Insert of "INVOLVES" relations between event and character
eventInvolveInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/events/involves.cyp'
with urllib.request.urlopen(eventInvolveInsertUrl) as url:
    eventInvolveInsert = url.read().decode()

GoT2Neo.run(eventInvolveInsert)

# Insert of "HAPPENS_IN" relations between event and scene
eventSceneInsertUrl = 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Cypher%20Scripts/creation/events/happensin.cyp'
with urllib.request.urlopen(eventSceneInsertUrl) as url:
    eventSceneInsert = url.read().decode()

GoT2Neo.run(eventSceneInsert)
