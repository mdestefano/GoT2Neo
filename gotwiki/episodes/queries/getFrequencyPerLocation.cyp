MATCH (s:Scene)-[si:SET_IN]->(l:Location)
WITH l, count(si) AS nSets
RETURN l.name, nSets ORDER BY nSets DESC