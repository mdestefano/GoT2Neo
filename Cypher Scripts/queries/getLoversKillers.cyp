MATCH
  (e:Event {kind: 'sex', type: 'love'})-[:INVOLVES]->(c1:Character), (e:Event)-[:INVOLVES]->(c2:Character)
  WHERE (c1)-[:KILLED]->(c2) OR (c2)-[:KILLED]->(c1)
RETURN e, c1, c2