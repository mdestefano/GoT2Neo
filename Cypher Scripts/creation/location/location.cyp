WITH 'https://raw.githubusercontent.com/mdestefano/GoT2Neo/master/Data/locations.json' AS url
CALL apoc.load.json(url) YIELD value
WITH value.regions AS regions
WITH [region IN regions | region] AS regions
FOREACH (region IN regions |
  MERGE(s:Location {
    name:         region.location,
    sublocations: region.subLocation
  })
)
