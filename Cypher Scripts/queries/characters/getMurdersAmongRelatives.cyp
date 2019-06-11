MATCH (killer:Character)-[k:KILLED]->(dead:Character)
MATCH path = (killer)-->(dead)
  WHERE any (r IN relationships(path)
    WHERE type(r) = 'SON_OF' OR type(r) = 'SIBLING_OF' OR type(r) = 'ENGAGED')
RETURN killer, k, dead, path