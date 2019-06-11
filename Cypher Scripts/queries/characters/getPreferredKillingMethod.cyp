MATCH (c:Character {name: 'Daenerys Targaryen'})-[k:KILLED]->(:Character)
  WHERE k.methodCat IS NOT NULL
WITH k.methodCat AS mc, count(k.methodCat) AS mcCount
  ORDER BY mcCount DESC
RETURN head(collect(mc))