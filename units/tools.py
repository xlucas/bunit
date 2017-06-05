from __future__ import division


def convert(value, unit_in, unit_out):
    return unit_in.value * value / unit_out.value


def lookup_system(unit_name, systems):
    for system in systems:
        for name, member in system.__members__.items():
            if name == unit_name:
                return system
