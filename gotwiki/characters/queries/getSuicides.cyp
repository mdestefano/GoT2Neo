MATCH p = (c1:Character)-[k:KILLED]->(c2:Character {name: c1.name})
WITH c1, count(k) AS nK
  WHERE nK = 1
RETURN c1 AS character