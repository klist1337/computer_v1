
import sys
from parser import parser
from helper import printError

if __name__ == "__main__":
    parsingRes = parser(sys.argv)
    printError(parsingRes)
    