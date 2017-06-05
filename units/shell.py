import argparse
import mmap
import sys

from prettytable import PrettyTable
from units import binary, si, tools


def build_parser():
    parser = argparse.ArgumentParser(description='Useful unit conversions')

    # Input nature
    parser.add_argument(
        '--in', metavar='unit', help='Input unit', required=True
    )
    parser.add_argument(
        '--precision', metavar='value', help='Precision', type=int, default=1
    )

    # Convert to single unit or whole unit system
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--out', metavar='unit', help='Output unit')
    group.add_argument('--system', metavar='system', help='Output unit system')

    return parser


def print_unit_system(value, unit_in, system, precision):
    table = PrettyTable(['Unit', 'Value'])
    for unit_out in system:
        converted_value = tools.convert(value, unit_in, unit_out)
        converted_value_string = '%.*f' % (precision, converted_value)
        table.add_row([unit_out.name, converted_value_string])
    print table


def main():
    raw_value = sys.stdin.read()
    parser = build_parser()
    parsed_args = parser.parse_args()

    systems = [binary.BiBytes, si.Bits, si.Bytes]

    unit_name_in = getattr(parsed_args, 'in')
    unit_name_out = getattr(parsed_args, 'out')

    system_in = tools.lookup_system(unit_name_in, systems)
    system_out = tools.lookup_system(unit_name_out, systems)


if __name__ == '__main__':
    sys.exit(main())
