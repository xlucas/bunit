import argparse
import mmap
import operator
import sys

from prettytable import PrettyTable
from units import binary, si, tools, errors


def build_parser():
    parser = argparse.ArgumentParser(description='Useful unit conversions')

    # Input
    parser.add_argument('--in', metavar='unit', required=True)

    # Output
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--out', metavar='unit')
    group.add_argument('--system', metavar='name')

    # Other options
    parser.add_argument('--precision', metavar='value', type=int, default=1)

    return parser


def print_unit_system(value, unit_in, system, precision):
    table = PrettyTable(['Unit', 'Value'])
    for unit_out in system:
        converted_value = tools.convert(value, unit_in, unit_out)
        converted_value_string = '%.*f' % (precision, converted_value)
        table.add_row([unit_out.name, converted_value_string])
    print table


def list_all_units(systems):
    return reduce(
        lambda x, y: x + y,
        [map(operator.attrgetter('name'), list(system)) for system in systems]
    )


def print_unit_error(unit_name, systems):
    units = ', '.join(list_all_units(systems))
    sys.stderr.write("Unrecognized unit '%s'\n" % unit_name)
    sys.stderr.write("Possible values are: %s" % units)


def main():
    parser = build_parser()
    parsed_args = parser.parse_args()

    try:
        value = float(sys.stdin.read())
    except ValueError:
        sys.stderr.write("Invalid input stream.")
        return errors.ERR_VAL

    systems = [si.Bits, si.Bytes, binary.BiBytes]

    unit_name_in = getattr(parsed_args, 'in')
    unit_name_out = getattr(parsed_args, 'out')

    system_in = tools.find_system(unit_name_in, systems)
    system_out = tools.find_system(unit_name_out, systems)

    if not system_in:
        print_unit_error(unit_name_in, systems)
        return errors.ERR_OPT

    if not system_out and unit_name_out:
        print_unit_error(unit_name_out, systems)
        return errors.ERR_OPT

    if not system_out:
        print_unit_system(
            value, system_in[unit_name_in], system_in, parsed_args.precision
        )
        return

    if unit_name_out:
        pass
        # TODO: convert & print the value
    else:
        pass
        # TODO: convert & print the system


if __name__ == '__main__':
    sys.exit(main())
