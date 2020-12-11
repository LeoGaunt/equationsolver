from sympy import symbols, solve
import matplotlib

expr = input('What is your expression?')

def solveForX():
    x = symbols('x')
    solx = solve(expr)
    print(solx)

def solveForY():
    y = symbols('y')
    soly = solve(expr)
    print(soly)

solveForX()
