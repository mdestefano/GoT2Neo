MATCH (c:Character), (s:Scene), (c)-[r:APPEARS_IN]->(s)
WITH c, count(s) AS nScenes
RETURN c, nScenes
  ORDER BY nScenes DESC