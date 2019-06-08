MATCH (s:Scene), (c:Character)
  WHERE c.name IN s.characters
MERGE (c)-[:APPEARS_IN]->(s)
