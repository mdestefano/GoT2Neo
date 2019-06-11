LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/game-of-thrones-deaths-data.csv'
AS row
MATCH (c1:Character {name: row.killer}), (c2:Character {name: row.character_killed})
CREATE (c1)-[r:KILLED {
  season:     toInt(row.season),
  episode:    toInt(row.episode),
  method:     row.method,
  methodCat:  row.method_cat,
  reason:     row.reason,
  location:   row.location,
  allegiance: row.allegiance,
  importance: toInt(coalesce(row.importance, '0'))
}]->(c2)
