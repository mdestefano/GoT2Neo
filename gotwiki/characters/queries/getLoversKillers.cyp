MATCH
  (c1:Character)<-[i1:INVOLVES]-(e:Event {kind: 'sex', type: 'love'})-[i2:INVOLVES]->(c2:Character), (c1)-[k]-(c2)
  WHERE type(k) = 'KILLED'
RETURN c1, i1, e, i2, c2, k