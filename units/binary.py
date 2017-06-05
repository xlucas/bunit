from enum import Enum


class BiBytes(Enum):
    kiB = 1 << 10
    MiB = 1 << 20
    GiB = 1 << 30
    TiB = 1 << 40
    PiB = 1 << 50
    EiB = 1 << 60
    ZiB = 1 << 70
    YiB = 1 << 80

    def to(system, unit):
        pass
