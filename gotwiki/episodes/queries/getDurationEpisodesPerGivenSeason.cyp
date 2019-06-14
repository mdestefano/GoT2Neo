MATCH (s:Scene{season:{season_var}})
WITH s.episode as episodes, s
WITH episodes, duration.inSeconds(s.start, s.end).seconds AS seconds
return episodes, toFloat(sum(seconds)) / 3600