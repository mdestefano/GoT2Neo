MATCH
  (c1:Character)<-[i1:INVOLVES]-(e:Event {kind: 'sex', type: 'love'})-[i2:INVOLVES]->(c2:Character),
  (c1)-[k:KILLED]->(c2)
RETURN c1 AS killer, k AS killing, c2 AS killed, collect(e) AS sexes