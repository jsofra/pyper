import clojure.core as _clj
from itertools import izip, izip_longest

comp = _clj.comp
juxt = _clj.juxt

#lzip = lambda s1, s2: _clj.seq(izip(s1, s2))

def pipe(*args):
    return reduce(lambda x, y: y(x), args)

def curry(fun, *args):
    return lambda arg: fun(*((arg,) + args))
