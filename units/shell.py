import argparse
import mmap
import sys

from prettytable import PrettyTable
from units import binary, si


def build_parser():
    parser = argparse.ArgumentParser(description='Useful unit conversions')

    # Input nature
    parser.add_argument(
        '--in', metavar='unit', help='Input unit', required=True
    )

    # Convert to single unit or whole unit system
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--out', metavar='unit', help='Output unit')
    group.add_argument(
        '--out-system', metavar='system', help='Output unit system'
    )

    # Page
    parser.add_argument(
        '--page-size',
        metavar='size',
        help='System page size (defaults to system page size)',
        default=mmap.PAGESIZE,
        type=int
    )

    return parser


def print_unit_system(value, unit_in, system):
    table = PrettyTable(['Unit', 'Value'])
    for unit_out in system:
        table.add_row(unit_out.name, system.convert(value, unit_in, unit_out))
    sys.stdout.write(table)


def main():
    raw_value = sys.stdin.read()
    parser = build_parser()
    parsed_args = parser.parse_args()

    unit_name_in = getattr(parsed_args, 'in')

    for system in [si.Bits, si.Bytes, binary.BiBytes]:
        for unit_name, unit_out in system.__members__.items():
            if unit_name == unit_name_in:
                print system


if __name__ == '__main__':
    sys.exit(main())
