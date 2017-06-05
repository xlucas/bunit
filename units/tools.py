from __future__ import division


def convert(value, unit_in, unit_out):
    return unit_in.value * value / unit_out.value


def lookup_enum(member_name, cls):
    for name, _ in cls.__members__.items():
        if name == member_name:
            return cls


def find_system(unit_name, systems):
    for system in systems:
        match = lookup_enum(unit_name, system)
        if match is not None:
            return match
