MATCH (c:Character {house: 'Stark'})
  WHERE NOT ()-[:KILLED]->(c)
RETURN c