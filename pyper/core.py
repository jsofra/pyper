import clojure.lang.rt as _RT
import clojure.core as _clj

PList = _RT.list
PVector = _RT.vector
PMap = _RT.map
PSet = _RT.set

into = _clj.into
count = _clj.count
#empty = _clj.empty
first = _clj.first
rest = _clj.rest
conj = _clj.conj
cons = _clj.cons
find = _clj.find
nth = _clj.nth
last = _clj.last
assoc = _clj.assoc
dissoc = _clj.dissoc
#getIn = getattr(_clj, 'get-in')
#updateIn = getattr(_clj, 'update-in')
#assocIn = getattr(_clj, 'assoc-in')
#fnil = _clj.fnil
disj = _clj.disj
pop = _clj.pop
peek = _clj.peek
#hash = _clj.hash
get = _clj.get
hasKey = getattr(_clj, 'contains?')
isEmpty = getattr(_clj, 'empty?')
reverse = _clj.reverse
take = _clj.take
drop = _clj.drop
partition = _clj.partition
#partitionBy = getattr(_clj, 'partition-by')
iterate = _clj.iterate
into = _clj.into
interpose = _clj.interpose
interleave = _clj.interleave
concat = _clj.concat
#flatten = _clj.flatten
keys = _clj.keys
vals = _clj.vals
#primSeq = getattr(_clj, 'prim-seq')
map = _clj.map
mapcat = _clj.mapcat
reduce = _clj.reduce
#reduce-kv = _clj.reduce-kv
filter = _clj.filter
remove = _clj.remove
some = _clj.some
every = getattr(_clj, 'every?')
#equals = _clj.=
range = _clj.range
repeat = _clj.repeat
#repeatedly = _clj.repeatedly
sort = _clj.sort
sortBy = getattr(_clj, 'sort-by')
#intoArray = getattr(_clj, 'into-array')

#list = _clj.list
#vector = _clj.vector
#hash-map = _clj.hash-map
zipmap = _clj.zipmap
#set = _clj.set
#sorted-set = _clj.sorted-set

def toPyper(coll):
    constr = None
    if isinstance(coll, list):
        constr = PVector
    elif isinstance(coll, tuple):
        constr = PList
    elif isinstance(coll, dict):
        constr = PMap
    elif isinstance(coll, set):
        constr = PSet
    else:
        return coll
    return constr(*[toPyper(x) for x in coll])

def pipe(*args):
    return reduce(lambda x, y: y(x), args)

def curry(fun, *args):
    return lambda arg: fun(*((arg,) + args))
