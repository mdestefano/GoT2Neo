MATCH (:Character{house: {house_var}})-[k:KILLED]->(:Character)
WITH k.location AS location, count(k.location) AS locationCount
RETURN location, locationCount ORDER BY locationCount DESC