import re 
from helper import FormatError

def getPolynome(member : str) :
     
     # parcours le polynome et split le polynome en monome 
     
     #get monome with regular expression 
     pattern = r"[-+]?\d*\.?\d+\*X\^\d*"
     monomes = re.findall(pattern, member)
     # suppress empty element
     monomes = [monome for monome in monomes if monome]
     return monomes


def isMonomeFormat(member: str) :
     pattern = r"[+-]"
     monomes = re.split(pattern, member)
     #monomes regular expression
     # pattern = r"[-+]?\d*\.?\d+\*X\^\d*"
     #suppress empty element 
     monomes = [monome for monome in monomes if monome]
     for x in range(len(monomes)) :
          pattern = fr"[-+]?\d*\.?\d+\*X\^{x}"
          if re.match(pattern, monomes[x]) == None:
               return 0
     return 1



def reductedForm(first: str, second:str) :
     first


def errorHandler(arg : list) :
     size = len(arg)
     inputLen = 0
     if size == 1 :
          return FormatError.NONEARG
     if size > 2 :
          return FormatError.MANYARG
     inputLen = len(arg[1])
     if inputLen == 0 or arg[1].isspace() :
          return FormatError.EMPTYSTRING
     #replace all white space by empty string
     input = re.sub('\s', "", arg[1])
     if input[0] == "+":
          return FormatError.WRONGFORMAT
     if input.find("=",0,len(input)) == -1 :
          return FormatError.WRONGFORMAT
     #Check if there is something after equal symbol
     part = input.split('=')
     firstMember = part[0]
     secondMember = part[1]
     if len(part[1]) == 0 :
          return FormatError.WRONGFORMAT
     #for a valid equation we must have at least a monome in first and second member
     firstMemberPoly = getPolynome(firstMember)
     secondMemberPoly = getPolynome(secondMember)
     if len(firstMemberPoly) == 0 or len(secondMemberPoly) == 0 :
          return FormatError.WRONGFORMAT 
     if isMonomeFormat(firstMember) == 0 or isMonomeFormat(secondMember) == 0 :
          return FormatError.WRONGFORMAT
     
def parser(arg: list) :
     result = errorHandler(arg)
     return result