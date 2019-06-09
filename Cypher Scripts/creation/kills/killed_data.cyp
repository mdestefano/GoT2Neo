WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/deaths.json' AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.deaths AS deaths
MATCH (c1:Character {name: deaths.killer}), (c2:Character {name: deaths.character_killed})
MERGE (c1)-[r:KILLED]->(c2)
SET r.season = deaths.season, r.episode = deaths.episode, r.location = deaths.location, r.method = deaths.method, r.
  methodCat = deaths.method_cat, r.reason = deaths.reason, r.allegiance = deaths.allegiance, r.importance = deaths.
  importance
