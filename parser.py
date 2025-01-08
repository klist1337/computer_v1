import re 
from helper import FormatError

def errorHandler(arg : list) :
     pattern = r"[A-Za-z@]"
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
def getPolynome() : 
     polynome = []
         

def parser(arg: list) :
     result = errorHandler(arg)
     return result