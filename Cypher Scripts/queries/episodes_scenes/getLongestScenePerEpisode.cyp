MATCH (e:Episode)<-[:BELONGS_TO]-(s:Scene)
WITH e,
     toFloat(duration.inSeconds(s.start, s.
       end).seconds) / 60.0 AS minutes
WITH e, max(minutes) AS maxMinutes
MATCH (e:Episode)<-[:BELONGS_TO]-(s:Scene)
  WHERE toFloat(duration.inSeconds(s.start, s.
    end).seconds) / 60.0 = maxMinutes
RETURN e, head(collect(s))