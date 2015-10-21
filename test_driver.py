#!/usr/bin/env python
__author__ = 'rhvonlehe'

from pos import Pos

def main():
    my_pos = Pos("28a29a3c154e458298357f5bf9ff3676", "Giz9y4cM")

    r = my_pos.employees()
    print r


if __name__ == "__main__":
    main()
