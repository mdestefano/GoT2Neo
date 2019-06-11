MATCH
  (c1:Character)-[:BELONGS_TO]->(h1:House {name: 'Stark'}), (c2:Character)-[:BELONGS_TO]->(h2:House {name: 'Targaryen'})
  WHERE (c1)-[:KILLED]->(c2) OR (c2)-[:KILLED]->(c1)
RETURN h1, c1, h2, c2