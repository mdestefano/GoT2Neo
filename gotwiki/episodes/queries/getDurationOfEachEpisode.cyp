MATCH (s:Scene), (e:Episode) 
WHERE s.episode = e.episode and s.season = e.season
WITH s.episode as episodes , e as episode, s 
WITH episodes, duration.inSeconds(s.start, s.end).seconds AS seconds, episode
ORDER BY episode.episodeGlobal return episode.episodeGlobal, toFloat(sum(seconds)) / 60 as durationInMIn