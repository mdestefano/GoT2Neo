MATCH (e:Episode)
WITH e.season AS season, e.viewers AS viewers
RETURN season, sum(viewers), avg(viewers), stDev(viewers)
  ORDER BY season