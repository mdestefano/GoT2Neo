WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/characters.json' AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.characters AS characters
UNWIND characters.houseName AS houseName
WITH houseName, characters.characterName AS characterName
MATCH (c:Character)
MATCH (h:House)
  WHERE c.name = characterName AND h.name = houseName
MERGE (c)-[:BELONGS_TO]->(h)

//MATCH (h:House)<-[:BELONGS_TO]-(c:Character) return h,c