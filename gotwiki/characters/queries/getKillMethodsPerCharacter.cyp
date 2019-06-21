MATCH (c:Character)-[k:KILLED]->(:Character)
WITH c, k.methodCat AS mc, count(k.methodCat) AS mcCount
  ORDER BY mcCount DESC
RETURN c AS character, collect(mc) AS methodCats, collect(mcCount) AS counts
  LIMIT 20