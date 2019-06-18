MATCH (c1:Character)-[e:ENGAGED]-(c2:Character), (c1)-[s:SON_OF|:SIBLING_OF]->(c2)
RETURN head(collect(c1)) AS first, head(collect(c2)) AS second, type(s) AS kinship
UNION
MATCH
  (c1:Character)<-[i1:INVOLVES]-(:Event {kind: 'sex'})-[i2:INVOLVES]->(c2:Character), (c1)-[s:SON_OF|:SIBLING_OF]->(c2)
RETURN head(collect(c1)) AS first, head(collect(c2)) AS second, type(s) AS kinship