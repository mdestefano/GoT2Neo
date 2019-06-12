WITH {data} as value
UNWIND value.characters AS characters
WITH characters.characterName AS characterName,
     characters.parentOf AS parentOf
MATCH (c1:Character {name: characterName}), (c2:Character)
  WHERE c2.name IN parentOf
MERGE (c2)-[r:SON_OF]->(c1)