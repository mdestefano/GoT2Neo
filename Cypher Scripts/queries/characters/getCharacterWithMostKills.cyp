MATCH (c:Character)-[r:KILLED]->()
WITH c, count(r) AS nKills
WITH max(nKills) AS maxKills
MATCH (c:Character)-[r:KILLED]->()
WITH c, count(r) AS nKills, maxKills
  WHERE nKills = maxKills
RETURN c, maxKills