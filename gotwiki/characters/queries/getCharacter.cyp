MATCH (c1:Character {name: {characterName}}), (c1)-[:APPEARS_IN]->(:Scene)-[:BELONGS_TO]->(e:Episode)
WITH DISTINCT c1, e 
ORDER BY e.season, e.episode
RETURN c1 AS character, collect(e) AS episodes