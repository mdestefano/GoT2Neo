MATCH (:Character)-[k:KILLED]->(:Character {house: 'Stark'})
WITH k.location AS location, count(k.location) AS locationCount
RETURN location, locationCount
  ORDER BY locationCount DESC