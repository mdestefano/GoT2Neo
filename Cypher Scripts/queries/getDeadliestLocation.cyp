MATCH (:Character)-[k:KILLED]->(:Character)
WITH k.location AS location, count(k.location) AS locationCount
  ORDER BY locationCount DESC
RETURN head(collect(location)), locationCount