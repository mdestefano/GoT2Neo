MATCH (s:Scene)
WITH duration.inSeconds(s.start, s.
  end).seconds AS seconds
RETURN toFloat(sum(seconds)) / 3600