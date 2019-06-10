WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/characters.json' AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.characters AS characters
WITH characters.characterName AS characterName,
     characters.houseName AS houseName,
     characters.actorName AS actorName,
     characters.characterImageFull AS characterImageFull,
     characters.characterImageThumb AS characterImageThumb,
     characters.nickname AS characterNickname,
     characters.royal AS characterIsRoyal
MERGE (c:Character {
  name:       characterName,
  house:      coalesce(houseName, 'unknown'),
  actor:      coalesce(actorName, 'N/A'),
  imageFull:  coalesce(characterImageFull, 'N/A'),
  imageThumb: coalesce(characterImageThumb, 'N/A'),
  nickname:   coalesce(characterNickname, 'None'),
  isRoyal:    toBoolean(coalesce(characterIsRoyal, 'false'))
})