MATCH (:Character)-[k:KILLED]->(:Character)
WITH k.season AS season, count(k.season) AS seasonKill
RETURN season, seasonKill ORDER BY season