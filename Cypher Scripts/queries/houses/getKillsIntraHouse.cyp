MATCH (c1:Character {house: 'Lannister'})-[k:KILLED]->(c2:Character {house: c1.house})
RETURN c1, k, c2