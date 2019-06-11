MATCH (e:Event {kind: 'sex'})-[h:HAPPENS_IN]->(s:Scene)
WITH toFloat(count(e)) AS totalCount
MATCH (e:Event {kind: 'sex'})-[h:HAPPENS_IN]->(s:Scene)
WITH s.season AS season, count(s.season) AS seasonCount, totalCount
WITH season, toFloat(seasonCount) / totalCount * 100 AS seasonPercentage
RETURN season, seasonPercentage