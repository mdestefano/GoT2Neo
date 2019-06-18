MATCH (episode:Episode)
WITH (episode.IMBD_Score + episode.RottenTomatoes_Score) / 2 AS meanScore, episode
ORDER BY meanScore RETURN episode, meanScore