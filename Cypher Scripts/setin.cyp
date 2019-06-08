MATCH (s:Scene), (l:Location {name: s.location})
MERGE (s)-[:SET_IN]->(l)
