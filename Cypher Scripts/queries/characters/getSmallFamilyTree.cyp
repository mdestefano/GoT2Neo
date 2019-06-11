match (c:Character{name:'Eddard Stark'})-[r1:SON_OF*1..5]->(m:Character)
optional match (q:Character)-[r2:SON_OF]->(c)
optional match(z:Character)-[r3:ENGAGED]->(c)
return c,m,q,z,r1,r2,r3