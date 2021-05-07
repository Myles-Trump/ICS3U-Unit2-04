#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates the cost of buying a pizza
#    based off their size


import constants


def main():
    # this function calculates the cost of the pizza

    # input
    diameter = int(input("Enter the diameter of the pizza (in): "))

    # process
    cost = (0.75 + 1.00 + diameter * 0.50) * constants.HST

    # output
    print("\nThe cost of your pizza is ${0}.".format(cost))


if __name__ == "__main__":
    main()
