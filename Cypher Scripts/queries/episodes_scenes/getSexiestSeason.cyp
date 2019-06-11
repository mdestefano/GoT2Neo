MATCH (e:Event {kind: 'sex'})-[h:HAPPENS_IN]->(s:Scene)
WITH s.season AS season, count(s.season) AS seasonCount
  ORDER BY seasonCount DESC
RETURN head(collect(season))