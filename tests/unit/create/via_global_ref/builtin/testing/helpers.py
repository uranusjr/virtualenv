from functools import reduce

from virtualenv.create.via_global_ref.builtin.ref import ExePathRefToDest, PathRef
from virtualenv.util.path import Path


def is_ref(source):
    return isinstance(source, PathRef)


def is_exe(source):
    return type(source) is ExePathRefToDest


def has_src(src):
    return lambda ref: ref.src.as_posix() == Path(src).as_posix()


def has_target(target):
    return lambda ref: ref.base == target


def apply_filter(values, function):
    return filter(function, values)


def filterby(filters, sources):
    return reduce(apply_filter, filters, sources)


def contains_exe(sources, src, target=None):
    filters = is_exe, has_src(src), target and has_target(target)
    return any(filterby(filters, sources))


def contains_ref(sources, src):
    filters = is_ref, has_src(src)
    return any(filterby(filters, sources))
