WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/episodes.json' AS url
CALL apoc.load.json(url) YIELD value
WITH value.episodes AS episodes
WITH [episode IN episodes | episode] AS episodesL
FOREACH (episode IN episodesL |
  FOREACH (scenesEpisode IN episode.scenes |
    FOREACH (scene IN scenesEpisode |
      CREATE(s:Scene {
        id:          scene.id,
        start:       localtime(scene.sceneStart),
        end:         localtime(scene.sceneEnd),
        season:      episode.seasonNum,
        episode:     episode.episodeNum,
        characters:  scene.characters,
        location:    scene.location,
        sublocation: coalesce(scene.subLocation, '')
      })
    )
  )
)