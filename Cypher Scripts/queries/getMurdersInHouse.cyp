MATCH (c1:Character {house: 'Lannister'})-[:KILLED]->(c2:Character {house: c1.house})
RETURN c1, c2