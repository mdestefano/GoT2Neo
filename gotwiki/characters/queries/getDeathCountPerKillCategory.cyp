MATCH (:Character)-[k:KILLED]->(:Character)
  WHERE k.methodCat IS NOT NULL
RETURN k.methodCat AS methodCat, count(k.methodCat) AS count
ORDER BY count DESC