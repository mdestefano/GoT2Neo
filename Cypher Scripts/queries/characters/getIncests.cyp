MATCH
  (c1:Character)-[s:SIBLING_OF]->(c2:Character), (c1)<-[i1:INVOLVES]-(e:Event {kind: 'sex'})-[i2:INVOLVES]->(c2)
RETURN c1, s, c2, i1, e, i2