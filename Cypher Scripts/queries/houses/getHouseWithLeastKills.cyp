MATCH (h:House), (c:Character {house: h.name}), (c)-[r:KILLED]->()
WITH h, count(r) AS nKills
WITH min(nKills) AS minKills
MATCH (h:House), (c:Character {house: h.name}), (c)-[r:KILLED]->()
WITH h, count(r) AS nKills, minKills
  WHERE nKills = minKills
RETURN h, minKills