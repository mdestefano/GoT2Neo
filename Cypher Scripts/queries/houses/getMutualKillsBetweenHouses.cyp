MATCH
  (c1:Character)-[b1:BELONGS_TO]->(h1:House {name: 'Greyjoy'}),
  (c2:Character)-[b2:BELONGS_TO]->(h2:House {name: 'Lannister'}), (c1)-[k:KILLED]-(c2)
RETURN h1, c1, h2, c2, k