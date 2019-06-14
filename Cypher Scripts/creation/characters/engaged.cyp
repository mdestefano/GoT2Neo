WITH {data} as value
UNWIND value.characters AS characters
WITH characters.characterName AS characterName,
     characters.marriedEngaged AS engaged
MATCH (c1:Character {name: characterName}), (c2:Character)
  WHERE c2.name IN engaged
MERGE (c1)-[r:ENGAGED]->(c2)
