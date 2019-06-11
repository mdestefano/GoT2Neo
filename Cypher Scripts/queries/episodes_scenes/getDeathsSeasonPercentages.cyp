MATCH (:Character)-[k:KILLED]->(:Character)
WITH count(k) AS totalKill
MATCH (:Character)-[k:KILLED]->(:Character)
WITH k.season AS season, count(k.season) AS seasonKill, totalKill
WITH season, toFloat(seasonKill) / totalKill * 100 AS seasonPercentage
RETURN season, seasonPercentage
  ORDER BY season