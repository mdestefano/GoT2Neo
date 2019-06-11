MATCH (e:Episode)
WITH e.season AS season, (e.IMBD_Score + e.RottenTomatoes_Score) / 2 AS epScore
RETURN season, avg(epScore), stDev(epScore)
  ORDER BY season