MATCH (c1:Character)-[k:KILLED]->(c2:Character)
MATCH path = (c1)-->(c2)
WITH c1, k, c2, relationships(path) AS rels
  WHERE any (r IN rels
    WHERE type(r) = 'SON_OF' OR type(r) = 'SIBLING_OF' OR type(r) = 'ENGAGED')
RETURN c1 AS killer, k AS killing, [r IN rels | type(r)] AS relTypes, c2 AS killed
  ORDER BY killing.season, killing.episode