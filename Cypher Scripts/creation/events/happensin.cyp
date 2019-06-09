MATCH (e:Event), (s:Scene {id: e.sceneId})
MERGE (e)-[:HAPPENS_IN]->(s)