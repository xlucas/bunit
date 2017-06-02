from __future__ import division


class System(object):
    @staticmethod
    def convert(value, unit_in, unit_out):
        return (unit_in.value * value) / unit_out.value

    def __contains__(self, item):
        pass
