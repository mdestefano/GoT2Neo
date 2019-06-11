LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/houses.csv' AS row
CREATE (h:House {
  name:     row.name,
  words:    row.words,
  region:   row.region,
  seat:     row.seat,
  lord:     row.lord,
  coa:      row.coa,
  alive:    toBoolean(coalesce(row.alive, 'false')),
  religion: row.religion
})