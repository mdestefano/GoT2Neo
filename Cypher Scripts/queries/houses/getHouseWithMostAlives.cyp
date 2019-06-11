MATCH (h:House), (c:Character {house: h.name})
  WHERE NOT ()-[:KILLED]->(c)
WITH h, count(c) AS nAlives
WITH max(nAlives) AS maxAlives
MATCH (h:House), (c:Character {house: h.name})
  WHERE NOT ()-[:KILLED]->(c)
WITH h, count(c) AS nAlives, maxAlives
  WHERE nAlives = maxAlives
RETURN h, maxAlives