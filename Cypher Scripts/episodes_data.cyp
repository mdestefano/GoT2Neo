LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/episodes_Scores.csv' AS row
MATCH (e:Episode {title: row.title})
SET e.episodeGlobal = row.episode, e.director = row.director, e.writer = row.writer, e.airDate = row.airDate, e.
  viewers = row.viewers, e.IMBD_Score = row.IMBD_Score, e.RottenTomatoes_Score = row.RottenTomatoes_Score
RETURN e