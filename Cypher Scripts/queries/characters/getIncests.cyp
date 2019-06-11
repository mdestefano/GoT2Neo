MATCH (c1:Character)-[e:ENGAGED]-(c2:Character)
MATCH (c1)-[s1]-(c2)
  WHERE (type(s1) = 'SON_OF' OR type(s1) = 'SIBLING_OF')
WITH c1, s1, c2
MATCH (c3:Character)<-[i1:INVOLVES]-(:Event {kind: 'sex'})-[i2:INVOLVES]->(c4:Character)
MATCH (c3)-[s2]-(c4)
  WHERE type(s2) = 'SON_OF' OR type(s2) = 'SIBLING_OF'
RETURN c1, s1, c2, c3, s2, c4