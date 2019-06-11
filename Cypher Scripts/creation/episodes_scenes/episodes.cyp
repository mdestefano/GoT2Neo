LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/episodes_Scores.csv' AS row
MERGE (e:Episode {
  title:                row.title,
  season:               toInt(row.season),
  episode:              toInt(row.episodeInSeason),
  episodeGlobal:        toInt(row.episode),
  director:             row.director,
  writer:               row.writer,
  airDate:              row.airDate,
  viewers:              toFloat(row.viewers),
  IMBD_Score:           toFloat(row.IMDB_Score),
  RottenTomatoes_Score: toFloat(row.RottenTomatoes_Score)
})