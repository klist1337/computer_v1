import re 
from helper import FormatError

def getPolynome(input : str) :
     
     # parcours le polynome et split le polynome en monome 
     polynome = []
     pattern = r"[+-]"
     print(input)
     polynome = re.split(pattern, input)
     print(polynome)
     


def errorHandler(arg : list) :
     pattern = r"[A-Wa-wxY:;,~yZz@&%$#!{}'<>\[\]\,?/()]"
     size = len(arg)
     inputLen = 0
     if size == 1 :
          return FormatError.NONEARG
     if size > 2 :
          return FormatError.MANYARG
     inputLen = len(arg[1])
     if inputLen == 0 or arg[1].isspace() :
          return FormatError.EMPTYSTRING
     if re.findall(pattern, arg[1]) != [] :
          return FormatError.WRONGFORMAT
     #replace all white space by empty string
     input = re.sub('\s', "", arg[1])
     if (input[0] == "+"):
          return FormatError.WRONGFORMAT
     getPolynome(input)

def parser(arg: list) :
     result = errorHandler(arg)

     return result