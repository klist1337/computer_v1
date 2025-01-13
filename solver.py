
from helper import *
import sys
from fractions import Fraction
import math

def degreeZeroSolver(parsingRes) :
    reducedForm = parsingRes[0]
    text = f"Reducted form: {reducedForm}"
    text += "\n" + f"Polynomial degree: {parsingRes[1]}"
    text += "\n" + "The solution is:" + "\n"
    text += "Each real is a solution"
    return text

def degreeGreatherThanTwo(parsingRes) :
    reducedForm  = parsingRes[0]
    text = f"Reducted form: {reducedForm}"
    text += "\n" + f"Polynomial degree: {parsingRes[1]}"
    text += "\n" + "The polynomial degree is strictly greater than 2,"
    text += " I can't solve."
    return text

def degreeOneSolver(parsingRes) :
    coeffs = parsingRes[3]
    reducedForm = parsingRes[0]
    text = f"Reducted form: {reducedForm}"
    text += "\n" + f"Polynomial degree: {parsingRes[1]}"
    try :
        res =  - 1 * float(coeffs[0] / coeffs[1])
    except ZeroDivisionError:
        text += "\n" + "The solution is:" + "\n"
        text += "Each real is a solution"  
        return text
    text += "\n" + "The solution is:" + "\n"
    text += f"{res}"
    text += "\n" + "The solution in irreductible form:"
    irr =  - Fraction(coeffs[0], coeffs[1])
    text += "\n" + f"{irr}"
    return text

def isDecimal(s) :
    stringFormat = str(s)
    part = stringFormat.split(".")
    if int(part[1]) == 0:
        return int(s)
    if len(part[1]) > 6:
        return "{0:.6}".format(s)
    return s

def degreeTwoSolver(parsingRes):
    coeffs = parsingRes[3]
    reducedForm = parsingRes[0]
    text = f"Reduced form: {reducedForm}"
    text += "\n" + f"Polynomial degree: {parsingRes[1]}"
    # delta = b^2 - 4ac
    delta =  coeffs[1] ** 2 -  4 * coeffs[2] * coeffs[0]
    # if delta is greather than 0 there is two solution
    if delta > 0 :   
        s1 = (- coeffs[1] - math.sqrt(delta)) / (2 * coeffs[2])
        s2 = (- coeffs[1]  + math.sqrt(delta)) / (2 * coeffs[2])
        text += "\n" + "Discriminant is strictly positive, the two solutions are: "
        text += "\n" + f"{isDecimal(s1)}"
        text += "\n" + f"{isDecimal(s2)}"
        text += "\n" + "The solutions in irreductible form:"
        irrS1 = Fraction(s1)
        irrS2 = Fraction (s2)
        text += "\n" + f"{irrS1}"
        text += "\n" + f"{irrS2}"
        return text
    if delta == 0 :
        #unique solution 
        s0 = - coeffs[1] / ( 2 * coeffs[2])
        text += "\n" + "the discriminant is equal to O, the unique solution is:"
        text += "\n" + f"{s0}"
        irr = Fraction(s0)
        text += "\n" + "The solutions in irreductible form:"
        text += "\n" + f"{irr}"
        return text
    if delta < 0:
        #two complexe solution
        sqrtDelta = math.sqrt(abs(delta))
        s1 = f"{- coeffs[0]}" + " + " + f"{sqrtDelta}i" + "/ " +  f"{2 * coeffs[2]}"
        s2 = f"{- coeffs[0]}" + " - " + f"{sqrtDelta}i" + "/ " +  f"{2 * coeffs[2]}"
        text += "\n" + "the discriminant is strictly negative, there is no reels solutions"
        text += "\n" + "The solutions are complex, the two solutions are:"
        text += "\n" + f"{s1}"
        text += "\n" + f"{s2}"
    return text

def solver(parsingRes) :
    match parsingRes[2]:
        case PolynomialDegree.Zero:
            return degreeZeroSolver(parsingRes)
        case PolynomialDegree.GREATHERTHANTWO :
            return degreeGreatherThanTwo(parsingRes)
        case PolynomialDegree.ONE :
            return degreeOneSolver(parsingRes) 
        case PolynomialDegree.TWO :
            return degreeTwoSolver(parsingRes)