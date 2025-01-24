
import sys
from parser import parser
from helper import printError
from solver import solver

if __name__ == "__main__":
    parsingRes = parser(sys.argv)
    printError(parsingRes)
    res = solver(parsingRes)
    print(res)