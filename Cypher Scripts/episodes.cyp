WITH 'https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/episodes.json' AS url
CALL apoc.load.json(url) YIELD value
UNWIND value.episodes AS episodes
WITH episodes.episodeTitle AS episodeTitle, episodes.seasonNum AS seasonNum, episodes.episodeNum AS episodeNum
MERGE (e:Episode {
  title:   episodeTitle,
  season:  seasonNum,
  episode: episodeNum
})
RETURN e
