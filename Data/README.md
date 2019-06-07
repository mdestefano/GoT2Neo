# Data description

- **game-of-thrones-deaths-data.csv**: The deaths of each season, with the cause and the people involved in it.
  - Fields of the CSV: (season, episode. character_killed, killer, method, method_cat, reason,	location,	allegiance,	importance)
- **episodes_Scores.csv**: The episodes of each season, the authors, the information related to the critic, the airing and the ratings
  - Fields of the CSV: (Title, Episode, Season, EpisodeInSeason, Director, Writer, AirDate, Viewers, IMDB_Score, RottenTomatoes_Score)
- **episodes.json**: Contains the description of each episode and each scene in the series.
  - The episodes are described with title, airing date, the summary of what happens and the location of the opening.
  - The data on the scenes instead show start and end times of the scene, the location, the characters that appear and any relevant events
- **location.json**: The locations of the series.
  - Each data is composed of the main location and the relative sub-locations
- **houses.csv**: The major houses in the series
  - Each record contains: house name, words, region, seat, current lord (s8), coat of arms, is alive (s8), religion
