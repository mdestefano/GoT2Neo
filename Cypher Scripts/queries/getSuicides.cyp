MATCH (c1:Character)-[:KILLED]->(c2:Character {name: c1.name})
RETURN c1, c2