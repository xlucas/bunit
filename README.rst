Units
=====

A dead simple unit conversion tool.


Usage
-----

Hereinafter are few examples of how to use this tool.


Converting between two units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    echo "1024" | units --in=kiB --out=MiB
    1.0

.. code-block::

    echo "128" | units --in=b --out=B
    16

Converting between units of the same system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    echo "32" | units --in=GiB
    +------+-------------+
    | Unit |    Value    |
    +------+-------------+
    | kiB  | 33554432.00 |
    | MiB  |   32768.00  |
    | GiB  |    32.00    |
    | TiB  |     0.03    |
    | PiB  |     0.00    |
    | EiB  |     0.00    |
    | ZiB  |     0.00    |
    | YiB  |     0.00    |
    +------+-------------+

Converting between units of different systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    echo "1" | units --in=GiB --system=bytes
    +------+---------------+
    | Unit |     Value     |
    +------+---------------+
    |  B   | 1073741824.00 |
    |  kB  |   1073741.82  |
    |  MB  |    1073.74    |
    |  GB  |      1.07     |
    |  TB  |      0.00     |
    |  PB  |      0.00     |
    |  EB  |      0.00     |
    |  ZB  |      0.00     |
    |  YB  |      0.00     |
    +------+---------------+
