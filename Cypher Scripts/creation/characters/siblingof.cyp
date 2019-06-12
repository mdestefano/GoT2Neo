WITH {data} as value
UNWIND value.characters AS characters
WITH characters.characterName AS characterName,
     characters.siblings AS siblings
MATCH (c1:Character {name: characterName}), (c2:Character)
  WHERE c2.name IN siblings
MERGE (c1)-[r:SIBLING_OF]->(c2)