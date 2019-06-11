MATCH (h:House), (:Character)-[k:KILLED]->(:Character {house: h.name})
RETURN h.name, count(k)
  ORDER BY count(k) DESC