MATCH (s:Scene)
WITH s.season as season,duration.inSeconds(s.start, s.end).seconds AS seconds
RETURN season, toFloat(sum(seconds)) / 3600