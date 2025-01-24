import re 
from helper import *

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
     #suppress empty element 
     monomes = [monome for monome in monomes if monome]
     for x in range(len(monomes)) :
          pattern = fr"^[-+]?\d*\.?\d+\*X\^{x}$"
          if re.match(pattern, monomes[x]) == None:
               return 0
     return 1


def getCoeff(monome: str) :
     part = monome.split('*')
     coefString = part[0]
     coef = float(coefString)
     return coef

def getAllCoeff(firstPoly, secondPoly) :
     coeffs = []
     if len(firstPoly) > len (secondPoly) :
          for x in range(len(firstPoly)):
               try:
                    coeffs.append(getCoeff(firstPoly[x]) - getCoeff(secondPoly[x]))
               except IndexError:
                    coeffs.append(getCoeff(firstPoly[x]))
     if (len(firstPoly) < len(secondPoly)) :
          for x in range(len(secondPoly)):
               try:
                    coeffs.append(getCoeff(firstPoly[x]) - getCoeff(secondPoly[x]))
               except IndexError :
                   coeffs.append(-getCoeff(secondPoly[x]))
     if len(firstPoly) == len(secondPoly) :
               for x in range(len(firstPoly)) :
                    coeffs.append(getCoeff(firstPoly[x]) - getCoeff(secondPoly[x]))
     return coeffs

def reducedForm(firstPoly: str, secondPoly:str) :
     #we have to check the longest polynome to iterate it for sommation
     coeffs = getAllCoeff(firstPoly, secondPoly)
     reduced = ""
     flag = 0
     for x in range(len(coeffs)) :
          if (coeffs[x] != 0) :
               flag = 1
               coeffsString = str(coeffs[x])
               part = coeffsString.split('.')
               if (int(part[1]) == 0) :
                    coeffs[x] = int(coeffs[x])
               if (coeffs[x] > 0 and x > 0) :
                    flg = 0 
                    for y in range(0, x):
                         if (coeffs[y] != 0):
                              flg = 1
                    if flg == 0:     
                         reduced += f" {coeffs[x]} * X^{x} "
                    else:
                         reduced += f" + {coeffs[x]} * X^{x} "
               elif (coeffs[x] < 0 and x == 0) :
                    reduced += f" - {abs(coeffs[x])} * X^{x} "
               elif (coeffs[x] > 0 and x == 0) :
                    reduced += f"{coeffs[x]} * X^{x} "
               else :
                    reduced += f" - {abs(coeffs[x])} * X^{x} "
     if flag == 0:
          reduced += " 0 = 0"
     else:
          reduced+= "= 0"
     reduced2 = reduced.split('=')[0]
     coeffsList = reduced2.split('*')
     len (coeffsList) == 2 
     if reduced == " 0 = 0" :
          return [reduced, 0, PolynomialDegree.EACHREALISASOLUTION]
     if len (coeffsList) == 2 :
          degree = coeffsList[1].split('^')[1]
          if int(degree) == 0 :
               return [reduced, 0, PolynomialDegree.NOSOLUTION]
          if int(degree) == 1:
               return [reduced, 1, PolynomialDegree.ONE, coeffs]
     if len(coeffs) > 3 :
          return [reduced, len(coeffs) - 1,PolynomialDegree.GREATHERTHANTWO] 
     if len(coeffs) == 2:
          return [reduced, len(coeffs) - 1,PolynomialDegree.ONE, coeffs]
     if len(coeffs) == 3:
          return [reduced, len(coeffs) - 1, PolynomialDegree.TWO, coeffs]

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
     reduced = reducedForm(firstMemberPoly, secondMemberPoly)
     return reduced


def parser(arg: list) :
     result = errorHandler(arg)
     return result