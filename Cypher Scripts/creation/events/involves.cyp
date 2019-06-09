MATCH (e:Event), (c:Character {name: e.main})
MERGE (e)-[:INVOLVES]->(c)
WITH e
MATCH (c:Character)
  WHERE c.name IN e.involved
MERGE (e)-[:INVOLVES]->(c)