MATCH (c:Character {house: 'Stark'})
  WHERE ()-[:KILLED]->(c)
RETURN c