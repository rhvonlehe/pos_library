#!/usr/bin/env python
__author__ = 'rhvonlehe'

import sys
sys.path.append('../')
from pos import Pos

def main():
    my_pos = Pos("28a29a3c154e458298357f5bf9ff3676", "Giz9y4cM")

    r = my_pos.employees()
    print
    employee_list = my_pos.employees1()
    print r
    for emp in employee_list:
        print emp.first_name()
    my_pos.revenue_centers()


if __name__ == "__main__":
    main()
