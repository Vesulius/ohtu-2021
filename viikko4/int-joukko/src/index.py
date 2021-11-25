import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()
    joukko2 = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)

    joukko2.lisaa(1)
    joukko2.lisaa(4)

    lisattavat = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for luku in lisattavat:
        print(joukko)
        joukko.lisaa(luku)

    print(joukko)


if __name__ == "__main__":
    main()
