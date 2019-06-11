MATCH (:Character)-[k:KILLED]->(:Character)
  WHERE k.methodCat IS NOT NULL
RETURN k.methodCat, count(k.methodCat)