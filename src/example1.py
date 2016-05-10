#!/usr/bin/env python
"""Simple example usage of terminaltables without any other dependencies.

Just prints sample text and exits.
"""

from __future__ import print_function

from terminaltables import AsciiTable, DoubleTable


table_data = [
    ['Platform', 'Years', 'Notes'],
    ['Mk5', '2007-2009', '\033[37;41mUnavailable\033[0m'],
    ['MKVI', '2009-2013', 'Might actually be Mk5.'],
]
table = AsciiTable(table_data, 'wangbin')
print()
print(table.table)

table = DoubleTable(table_data, 'Jetta SportWagen')
table.inner_row_border = True
table.justify_columns[2] = 'right'
print()
print(table.table)

table.outer_border = False
table.justify_columns[1] = 'center'
print()
print(table.table)

print()
