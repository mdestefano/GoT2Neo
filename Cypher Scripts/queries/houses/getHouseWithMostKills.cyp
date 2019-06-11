MATCH (h:House), (c:Character {house: h.name}), (c)-[r:KILLED]->()
WITH h, count(r) AS nKills
WITH max(nKills) AS maxKills
MATCH (h:House), (c:Character {house: h.name}), (c)-[r:KILLED]->()
WITH h, count(r) AS nKills, maxKills
  WHERE nKills = maxKills
RETURN h, maxKills