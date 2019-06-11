MATCH (h:House), (c:Character {house: h.name}), (c)-[r:KILLED]->()
WITH h, count(r) AS nKills
RETURN h, nKills
  ORDER BY nKills DESC