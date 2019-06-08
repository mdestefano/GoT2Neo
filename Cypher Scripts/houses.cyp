LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/houses.csv' AS line
MERGE (h:House {
  name:     line.name,
  words:    line.words,
  region:   line.region,
  seat:     line.seat,
  lord:     line.lord,
  coa:      line.coa,
  alive:    line.alive,
  religion: line.religion
})
RETURN h