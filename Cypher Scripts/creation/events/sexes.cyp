WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/sexes.json' AS url
CALL apoc.load.json(url) YIELD value
WITH value.sexes AS sexes
UNWIND sexes AS sexesU
MERGE (e:Event {sceneId: sexesU.sceneId})
SET e = {
  sceneId:  sexesU.sceneId,
  main:     sexesU.character,
  involved: sexesU.with,
  kind:     'sex',
  type:     sexesU.type,
  when:     sexesU.when
}