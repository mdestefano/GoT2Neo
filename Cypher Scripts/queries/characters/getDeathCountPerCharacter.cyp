MATCH (c:Character)-[k:KILLED]->(:Character)
RETURN c, count(k)