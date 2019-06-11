MATCH (s:Scene)
WITH
  toFloat(duration.inSeconds(s.start, s.
    end).seconds) / 60.0 AS minutes, s
WITH s, minutes
  ORDER BY minutes DESC
  LIMIT 5
MATCH (c:Character)-[:APPEARS_IN]->(s)
RETURN DISTINCT c