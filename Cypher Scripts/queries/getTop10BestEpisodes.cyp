MATCH (e:Episode)
WITH (e.IMBD_Score + e.RottenTomatoes_Score) / 2 AS meanScore, e
  ORDER BY meanScore DESC
RETURN e, meanScore
  LIMIT 10