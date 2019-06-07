WITH "https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/characters.json" AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.characters AS characters
WITH characters.characterName AS characterName, 
     characters.houseName AS houseName,
     characters.actorName AS actorName, 
     characters.characterImageFull AS characterImage, 
     characters.nickname AS characterNickname
MERGE (c:Character{
        name:characterName,
        house:coalesce(houseName,"unknown"),
        actor:coalesce(actorName,"N/A"),
        image:coalesce(characterImage,"N/A"),
        nickname:coalesce(characterNickname,"None")
        })
RETURN c