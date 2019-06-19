MATCH
(h1:House{name:'Lannister'})<-[:BELONGS_TO]-(c1:Character)-[k:KILLED]->(c2:Character)-[:BELONGS_TO]->(h2:House)
with h2.name as target, count(c2) as kills
with max(kills) as maximum
MATCH
(h1:House{name:'Lannister'})<-[:BELONGS_TO]-(c1:Character)-[k:KILLED]->(c2:Character)-[:BELONGS_TO]->(h2:House)
with h2.name as target, count(c2) as kills, maximum
where kills = maximum
return target