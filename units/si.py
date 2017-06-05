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
    B = 10**0
    kB = 10**3
    MB = 10**6
    GB = 10**9
    TB = 10**12
    PB = 10**15
    EB = 10**18
    ZB = 10**21
    YB = 10**24
