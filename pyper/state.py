import clojure.core as _clj

atom = _clj.atom
deref = _clj.deref
swap_ = getattr(_clj, 'swap!')
reset_ = getattr(_clj, 'reset!')
