MATCH
  (c1:Character)-[b1:BELONGS_TO]->(h1:House {name: 'Baratheon'}),
  (c2:Character)-[b2:BELONGS_TO]->(h2:House {name: 'Lannister'}),
  (c1)<-[i1:INVOLVES]-(e:Event {kind: 'sex'})-[i2:INVOLVES]->(c2)
RETURN c1, b1, h1, c2, b2, h2, e, i1, i2