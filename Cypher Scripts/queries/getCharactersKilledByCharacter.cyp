MATCH (c1:Character {name: 'Drogon'}), (c2:Character), (c1)-[r:KILLED]->(c2)
RETURN c1, r, c2