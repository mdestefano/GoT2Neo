MATCH (c:Character)-[k:KILLED]->(:Character)
WITH c AS character, count(k) AS count
RETURN character, count
  ORDER BY count DESC
  LIMIT 20