WITH 'https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json' AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.characters AS characters
WITH characters.characterName AS characterName, characters.killed AS killed
MATCH (c1:Character)
  WHERE c1.name = characterName
MATCH (c2:Character)
  WHERE c2.name IN killed
MERGE (c1)-[:KILLED]->(c2)
RETURN c1, c2
