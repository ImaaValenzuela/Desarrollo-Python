from ast import arg
import re


def promedio(*args):
    return sum(args) / len(args)

resultado = promedio(10, 9, 5, 7, 10)


def combinacion (p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)


combinacion(10, 20, 1, 2, 3, 4, 5, p4=500)
