MATCH (c:Character {name: 'Joffrey Baratheon'})-[r:SON_OF|:SIBLING_OF]->(rel:Character)
WITH c, r, rel
OPTIONAL MATCH (rel)-[s1:SON_OF]->(gpar)
WITH c, r, rel, s1, gpar
OPTIONAL MATCH (son:Character)-[s2:SON_OF]->(c)
RETURN c, r, rel, s1, gpar, s2, son