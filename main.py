#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates the cost of buying a pizza
#    based off their size


def main():
    # this function calculates the cost of the pizza

    # input
    radius = int(input("Enter the radius of the pizza (in): "))

    # process
    cost = 0.75 + 1.00 + radius

    # output
    print("\nThe cost of your pizza is ${0}.".format(cost))


if __name__ == "__main__":
    main()
