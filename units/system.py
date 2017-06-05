from enum import Enum


class Bits(Enum):
    b = 10**0
    kb = 10**3
    Mb = 10**6
    Gb = 10**9
    Tb = 10**12
    Pb = 10**15
    Eb = 10**18
    Zb = 10**21
    Yb = 10**24


class Bytes(Enum):
    B = 8 * 10**0
    kB = 8 * 10**3
    MB = 8 * 10**6
    GB = 8 * 10**9
    TB = 8 * 10**12
    PB = 8 * 10**15
    EB = 8 * 10**18
    ZB = 8 * 10**21
    YB = 8 * 10**24


class BiBytes(Enum):
    kiB = 8 * 1 << 10
    MiB = 8 * 1 << 20
    GiB = 8 * 1 << 30
    TiB = 8 * 1 << 40
    PiB = 8 * 1 << 50
    EiB = 8 * 1 << 60
    ZiB = 8 * 1 << 70
    YiB = 8 * 1 << 80
