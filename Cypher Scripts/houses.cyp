LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/houses.csv' AS line
MERGE (h:House {
  name:     line.name,
  words:    line.words,
  region:   line.region,
  seat:     line.seat,
  lord:     line.lord,
  coa:      line.coa,
  alive:    toBoolean(line.alive),
  religion: line.religion
})
RETURN h

/*
WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/houses.json' AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.houses AS houses
MERGE
  (h:House {name: houses.name, words: houses.words, region: houses.region, seat: houses.seat, lord: houses.lord,
            coa:  houses.coa, alive: toBoolean(houses.alive), religion: houses.religion})
RETURN h
*/