MATCH (s:Scene)
WITH duration.inSeconds(s.start, s.
  end).seconds AS length
WITH max(length) AS maxLength
MATCH (s:Scene)
  WHERE duration.inSeconds(s.start, s.
    end).seconds = maxLength
RETURN s, maxLength