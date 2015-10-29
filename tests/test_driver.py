#!/usr/bin/env python
__author__ = 'rhvonlehe'

import sys
sys.path.append('../')
from pos import Pos

def main():
    my_pos = Pos("28a29a3c154e458298357f5bf9ff3676", "Giz9y4cM")

    employee_list = my_pos.employees()
    for emp in employee_list:
        print emp.first_name()

    print
    revenue_center_list = my_pos.revenue_centers()
    for rev in revenue_center_list:
        print rev.name()

    my_pos.create_ticket(employee_list[0], 'KxiAaip5', revenue_center_list[0], 'jLiyniEb', 1, 'auto_ticket')


if __name__ == "__main__":
    main()
