MATCH (c:Character {name: {character_name}})-[r1:SON_OF]->(m:Character)
OPTIONAL MATCH (m:Character)-[r2:SON_OF]->(g:Character)
OPTIONAL MATCH (q:Character)-[r3:SON_OF]->(c)
OPTIONAL MATCH (z:Character)-[r4:ENGAGED]->(c)
RETURN c AS characters, m AS parents, collect(DISTINCT g) AS gparents, collect(DISTINCT q) AS sons,
       collect(DISTINCT z) AS engages