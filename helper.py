from enum import Enum
import sys


class FormatError(Enum) :
     NONEARG = 0
     MANYARG = 1
     EMPTYSTRING = 2
     WRONGFORMAT = 3



def printError(parsingRes) :
    if parsingRes == FormatError.NONEARG :
        sys.exit("Please give the equation to solve") 
    if parsingRes == FormatError.MANYARG:
        sys.exit("You must give one argument: the equation only")
    if parsingRes == FormatError.EMPTYSTRING :
        sys.exit("Equation is empty")
    if parsingRes == FormatError.WRONGFORMAT :
        sys.exit("Your equation is wrong formated\n" 
                 "a * X^0 + b * X^1 = 0 (1st degree) where a, b and c are reels\n"
                 "a * X^0 + b * X^1 + c * X^2 = 0 (2nd degree) where a, b and c are reels")