MATCH (c:Character)-[:BELONGS_TO]->(h:House)
  WHERE NOT ()-[:KILLED]->(c)
RETURN h.name, count(c)
  ORDER BY count(c) DESC