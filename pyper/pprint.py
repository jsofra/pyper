from clojure.lang.indexableseq import IndexableSeq
from clojure.lang.persistenthashmap import PersistentHashMap
from clojure.lang.persistentvector import PersistentVector
from clojure.lang.persistenthashset import PersistentHashSet
from clojure.lang.persistentlist import PersistentList, EmptyList
from clojure.lang.iseq import ISeq

def _monkeypatch_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

def _pprintISeq(coll, pre="seq(", post=")", sep=", "):
    s = []
    remainder = coll
    while remainder:
        c.append(str(remainder.first()))
        remainder = remainder.next()
    return pre + sep.join(s) + post

def _pprintIndexableSeq(coll, pre="IndexableSeq([", post="])", sep=", "):
    s = []
    for x in range(coll.i, len(coll.array)):
        s.append(str(coll.array[x]))
    return pre + sep.join(s) + post

def _pprintPersistentHashMap(coll, pre="PMap(", post=")", sep=", ", entrysep=", "):
    s = []
    for x in coll:
        s.append(repr(x))
        s.append(entrysep)
        s.append(repr(coll[x]))
        s.append(sep)
    s.pop()
    return pre + "".join(s) + post

def _pprintPersistentVector(coll, pre="PVector(", post=")", sep=", "):
    s = []
    for x in coll:
        s.append(str(x))
    return pre + sep.join(s) + post

def _pprintPersistentHashSet(coll, pre="PSet(", post=")", sep=", "):
    s = []
    sq = coll.seq()
    while sq is not None:
        s.append(str(sq.first()))
        sq = sq.next()
    if not s:
        return pre + post
    else:
        return pre + sep.join(s) + post

def _pprintPersistentList(coll, pre="PList(", post=")", sep=", "):
    s = []
    for x in coll:
        s.append(str(x))
    return pre + sep.join(s) + post

def _pprintEmptyList(coll, pre="PList(", post=")", sep=", "):
    return pre + post

def setPyperPPrint():

    @_monkeypatch_method(ISeq)
    def __repr__(self):
        return _pprintISeq(self)

    @_monkeypatch_method(IndexableSeq)
    def __repr__(self):
        return _pprintIndexableSeq(self)

    @_monkeypatch_method(PersistentHashMap)
    def __repr__(self):
        return _pprintPersistentHashMap(self)

    @_monkeypatch_method(PersistentVector)
    def __repr__(self):
        return _pprintPersistentVector(self)

    @_monkeypatch_method(PersistentHashSet)
    def __repr__(self):
        return _pprintPersistentHashSet(self)

    @_monkeypatch_method(PersistentList)
    def __repr__(self):
        return _pprintPersistentList(self)

    @_monkeypatch_method(EmptyList)
    def __repr__(self):
        return _pprintEmptyList(self)


def setPyPPrint():

    @_monkeypatch_method(ISeq)
    def __repr__(self):
        return _pprintISeq(self, "(", ")")

    @_monkeypatch_method(IndexableSeq)
    def __repr__(self):
        return _pprintIndexableSeq(self, "(", ")")

    @_monkeypatch_method(PersistentHashMap)
    def __repr__(self):
        return _pprintPersistentHashMap(self, "{", "}", ", ", ": ")

    @_monkeypatch_method(PersistentVector)
    def __repr__(self):
        return _pprintPersistentVector(self, "[", "]")

    @_monkeypatch_method(PersistentHashSet)
    def __repr__(self):
        return _pprintPersistentHashSet(self, "set([", "])")

    @_monkeypatch_method(PersistentList)
    def __repr__(self):
        return _pprintPersistentList(self, "(", ")")

    @_monkeypatch_method(EmptyList)
    def __repr__(self):
        return _pprintEmptyList(self, "(", ")")


def setCljPPrint():

    @_monkeypatch_method(IndexableSeq)
    def __repr__(self):
        return _pprintIndexableSeq(self, "(", ")")

    @_monkeypatch_method(PersistentHashMap)
    def __repr__(self):
        return _pprintPersistentHashMap(self, "{", "}", ", ", " ")

    @_monkeypatch_method(PersistentVector)
    def __repr__(self):
        return _pprintPersistentVector(self, "[", "]")

    @_monkeypatch_method(PersistentHashSet)
    def __repr__(self):
        return _pprintPersistentHashSet(self, "#{", "}")

    @_monkeypatch_method(PersistentList)
    def __repr__(self):
        return _pprintPersistentList(self, "(", ")")

    @_monkeypatch_method(EmptyList)
    def __repr__(self):
        return _pprintEmptyList(self, "(", ")")
