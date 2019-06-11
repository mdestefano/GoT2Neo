MATCH (s:Scene)-[si:SET_IN]->(l:Location)
WITH l, count(si) AS nSets
WITH max(nSets) AS maxSets
MATCH (s:Scene)-[si:SET_IN]->(l:Location)
WITH l, maxSets, count(si) AS nSets
  WHERE nSets = maxSets
RETURN l, nSets