MATCH (s:Scene)
WITH
  toFloat(duration.inSeconds(s.start, s.
    end).seconds) / 60.0 AS minutes, s
RETURN s, minutes
  ORDER BY minutes DESC
  LIMIT 10