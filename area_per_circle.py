#!/usr/bin/env python3

# Created by: Carolyn Webster Pless
# Created on: 22/09/21
# Calculates area and perimeter of a circle with a radius of 15mm


import math


def main():
    print("For a circle with a radius of 15mm:")
    print("Area of the circle = {}mm^2".format(math.pi*15**2))
    print("Perimeter of the circle = {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
