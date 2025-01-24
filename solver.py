
from helper import *
import sys
from fractions import Fraction
import math

def noSolutionSolver(parsingRes) :
    reducedForm = parsingRes[0]
    text = f"Reducted form: {reducedForm}"
    text += "\n" + f"Polynomial degree: {parsingRes[1]}"
    text += "\n" + "This equation has no solution"
    return text

def eachRealIsSolution(parsingRes) :
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
    res = isDecimal(res)
    text += f"{res}"
    if (res != 0) :
        text += "\n" + "The solution in irreductible form:"
        try:
            irr =  - Fraction(coeffs[0], coeffs[1])
        except TypeError:
            irr = Fraction(res)
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
        numerator1 = - coeffs[1] - math.sqrt(delta)
        numerator2 = - coeffs[1]  + math.sqrt(delta)
        denominator =    2 * coeffs[2]
        s1 = numerator1 / denominator
        s2 = numerator2 / denominator
        text += "\n" + "Discriminant is strictly positive, the two solutions are: "
        text += "\n" + f"{isDecimal(s1)}"
        text += "\n" + f"{isDecimal(s2)}"
        text += "\n" + "The solutions in irreductible form:"
        try :
            irrS1 = Fraction(numerator1, denominator)
            irrS2 = Fraction (numerator2, denominator)
        except TypeError:
            print(numerator1, denominator)
            irrS1 = Fraction(s1)
            irrS2 = Fraction(s2)
        text += "\n" + f"{irrS1}"
        text += "\n" + f"{irrS2}"
        return text
    if delta == 0 :
        #unique solution
        numerator = - coeffs[1]
        denominator =  2 * coeffs[2]
        s0 = numerator / denominator
        text += "\n" + "the discriminant is equal to O, the unique solution is:"
        if s0 == - 0.0:
            s0 = 0
        text += "\n" + f"{s0}"
        try:
            irr = Fraction(numerator, denominator)
        except TypeError:
            irr = Fraction(s0)
        text += "\n" + "The solutions in irreductible form:"
        text += "\n" + f"{irr}"
        return text
    if delta < 0:
        #two complexe solution
        imag = math.sqrt(abs(delta)) / (2 * coeffs[2])
        real =  - coeffs[0] / (2  * coeffs[2])
        s1 = f"{real}" + " + " + f"{imag}i"
        s2 = f"{real}" + " - " + f"{imag}i"
        text += "\n" + "the discriminant is strictly negative, there is no reels solutions"
        text += "\n" + "The solutions are complex, the two solutions are:"
        text += "\n" + f"{s1}"
        text += "\n" + f"{s2}"
    return text

def solver(parsingRes) :
    match parsingRes[2]:
        case PolynomialDegree.NOSOLUTION:
            return noSolutionSolver(parsingRes)
        case PolynomialDegree.EACHREALISASOLUTION:
            return eachRealIsSolution(parsingRes)
        case PolynomialDegree.GREATHERTHANTWO :
            return degreeGreatherThanTwo(parsingRes)
        case PolynomialDegree.ONE :
            return degreeOneSolver(parsingRes) 
        case PolynomialDegree.TWO :
            return degreeTwoSolver(parsingRes)