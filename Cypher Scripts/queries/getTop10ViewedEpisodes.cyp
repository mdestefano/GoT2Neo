MATCH (e:Episode)
RETURN e
  ORDER BY e.viewers DESC
  LIMIT 10