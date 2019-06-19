MATCH
  (c1:Character)-[b1:BELONGS_TO]->(h1:House {name: 'Baratheon'}),
  (c2:Character)-[b2:BELONGS_TO]->(h2:House {name: 'Lannister'}), 
  (c1)-[k:KILLED]-(c2)
RETURN (startNode(k).name) as killer, (endNode(k).name) as killed