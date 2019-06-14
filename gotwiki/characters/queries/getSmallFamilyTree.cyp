MATCH (c:Character {name: {character_name}})-[r1:SON_OF*1..5]->(m:Character)
OPTIONAL MATCH (q:Character)-[r2:SON_OF]->(c)
OPTIONAL MATCH(z:Character)-[r3:ENGAGED]->(c)
RETURN c, m, q, z, r1, r2, r3