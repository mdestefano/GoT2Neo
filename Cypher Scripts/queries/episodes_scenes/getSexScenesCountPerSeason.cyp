MATCH (e:Event {kind: 'sex'})-[h:HAPPENS_IN]->(s:Scene)
WITH s.season AS season, count(s.season) AS seasonCount
RETURN season, seasonCount
  ORDER BY seasonCount DESC