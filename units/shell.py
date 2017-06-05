import argparse
import operator
import sys

from prettytable import PrettyTable
from units import system, tools, errors


def build_parser():
    parser = argparse.ArgumentParser(description='Useful unit conversions')

    # Input
    parser.add_argument('--in', metavar='unit', required=True)

    # Output
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--out', metavar='unit')
    group.add_argument('--system', metavar='name')

    # Other options
    parser.add_argument('--precision', metavar='value', type=int, default=2)

    return parser


def print_unit_system(value, unit_in, s, precision):
    table = PrettyTable(['Unit', 'Value'])
    for unit_out in s:
        converted_value = tools.convert(value, unit_in, unit_out)
        converted_value_string = '%.*f' % (precision, converted_value)
        table.add_row([unit_out.name, converted_value_string])
    print table


def list_all_units(systems):
    return reduce(
        lambda x, y: x + y,
        [map(operator.attrgetter('name'), list(s)) for s in systems]
    )


def print_unit_error(unit_name, systems):
    units = ', '.join(list_all_units(systems))
    sys.stderr.write("Unrecognized unit '%s'.\n" % unit_name)
    sys.stderr.write("Possible values are: %s" % units)


def main():
    parser = build_parser()
    parsed_args = parser.parse_args()

    try:
        value = float(sys.stdin.read())
    except ValueError:
        sys.stderr.write("Invalid input stream.")
        return errors.ERR_VAL

    systems = {
        'bits': system.Bits,
        'bytes': system.Bytes,
        'bibytes': system.BiBytes
    }

    unit_name_in = getattr(parsed_args, 'in')
    unit_name_out = getattr(parsed_args, 'out')
    system_name = getattr(parsed_args, 'system')

    system_in = tools.find_system(unit_name_in, systems.values())
    system_out = tools.find_system(unit_name_out, systems.values())

    if not system_in:
        print_unit_error(unit_name_in, systems.values())
        return errors.ERR_OPT

    if not system_out and unit_name_out:
        print_unit_error(unit_name_out, systems.values())
        return errors.ERR_OPT

    if system_name and not system_out:
        if system_name not in systems:
            names = ', '.join(systems.keys())
            sys.stderr.write("Unrecognized system name '%s'.\n" % system_name)
            sys.stderr.write("Possible values are: %s" % names)
            return errors.ERR_OPT
        else:
            system_out = systems[system_name]

    unit_in = system_in[unit_name_in]

    if not system_out:
        print_unit_system(value, unit_in, system_in, parsed_args.precision)
        return

    if unit_name_out:
        unit_out = system_out[unit_name_out]
        print(tools.convert(value, unit_in, unit_out))
    else:
        print_unit_system(value, unit_in, system_out, parsed_args.precision)


if __name__ == '__main__':
    sys.exit(main())
