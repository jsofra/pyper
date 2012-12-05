import clojure.set as _set

# Set ops
union = _set.union
intersection = _set.intersection
difference = _set.difference
select = _set.select
project = _set.project
renameKeys = getattr(_set, 'rename-keys')
rename = _set.rename
index = _set.index
mapInvert = getattr(_set, 'map-invert')
join = _set.join
isSubset = getattr(_set, 'subset?')
isSuperset = getattr(_set, 'superset?')
