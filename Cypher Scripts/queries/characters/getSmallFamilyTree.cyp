OPTIONAL MATCH (c:Character {name: 'Joffrey Baratheon'})-[son_r:SON_OF*1..2]->(par:Character)
WITH c, son_r, par
OPTIONAL MATCH (c)-[sib_r:SIBLING_OF]->(sib:Character)
WITH c, son_r, par, sib_r, sib
OPTIONAL MATCH (c)-[eng_r:ENGAGED]->(eng:Character)
RETURN c, son_r, par, sib_r, sib, eng_r, eng