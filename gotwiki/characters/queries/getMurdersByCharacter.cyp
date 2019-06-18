MATCH (c1:Character {name: {characterName}})-[r:KILLED]->(c2:Character)
RETURN DISTINCT c2 AS dead, c1 AS killer, collect(r) AS killings, count(r) AS count
  ORDER BY dead.name