from enum import Enum
from system import System


class Bits(System, Enum):
    b = 10**0
    kb = 10**3,
    Mb = 10**6,
    Gb = 10**9,
    Tb = 10**12,
    Pb = 10**15,
    Eb = 10**18,
    Zb = 10**21,
    Yb = 10**24,


class Bytes(System, Enum):
    B = 8 * 10**0,
    kB = 8 * 10**3,
    MB = 8 * 10**6,
    GB = 8 * 10**9,
    TB = 8 * 10**12,
    PB = 8 * 10**15,
    EB = 8 * 10**18,
    ZB = 8 * 10**21,
    YB = 8 * 10**24,
