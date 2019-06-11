MATCH
  (c1:Character)-[:BELONGS_TO]->(h1:House {name: 'Baratheon'}),
  (c2:Character)-[:BELONGS_TO]->(h2:House {name: 'Lannister'}), (e:Event {kind: 'sex'})
  WHERE (e)-[:INVOLVES]->(c1) AND (e)-[:INVOLVES]->(c2)
RETURN e, h1, c1, h2, c2