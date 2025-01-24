from enum import Enum
import sys


class FormatError(Enum) :
     NONEARG = 0
     MANYARG = 1
     EMPTYSTRING = 2
     WRONGFORMAT = 3
     BADPOLYNOME = 4

class PolynomialDegree(Enum) :
    NOSOLUTION = 0
    EACHREALISASOLUTION = 1
    ONE = 2
    TWO = 3
    GREATHERTHANTWO = 4


def printError(parsingRes) :
    str1 = "c * X^0 + b * X^1 = c * X^0 (1st degree) where a and b are reels"
    str2 = "c * X^0 + b * X^1 + a * X^2 = c * X^0 (2nd degree) where a, b and c are reels"
    format = "USAGE:\n" + str1 + '\n' + str2
    match parsingRes:
        case FormatError.NONEARG :
            sys.exit("Please give the equation to solve\n" + format) 
        case FormatError.MANYARG:
            sys.exit("You must give one argument: the equation only\n" + format)
        case FormatError.EMPTYSTRING :
            sys.exit("Equation is empty\n" + format)
        case FormatError.WRONGFORMAT :
            sys.exit("Your equation is wrong formated\n" + format)
        case FormatError.BADPOLYNOME:
            sys.exit("bad polynome\n" + format)