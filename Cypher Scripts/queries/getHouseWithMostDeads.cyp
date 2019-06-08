MATCH (h:House), (c:Character {house: h.name}), ()-[r:KILLED]->(c)
WITH h, count(r) AS nDeaths
WITH max(nDeaths) AS maxDeaths
MATCH (h:House), (c:Character {house: h.name}), ()-[r:KILLED]->(c)
WITH h, count(r) AS nDeaths, maxDeaths
  WHERE nDeaths = maxDeaths
RETURN h, maxDeaths