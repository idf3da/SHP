from math import sqrt
import os

def int_input():
    try:
        n = input()
    except:
        print("Что? What?")
    try:
        n = int(n)
    except:
        print("Number not convertable to int")
        exit(1)
    return n

class BaseEquationSolver():
    def __init__(self):
        self.vars = {}
        self.equation_type = "None"
        self.solutions = []

    def input_equation_type(self):
        self.equation_type = input("Equation type: ")
        
    def input_vars(self):
        for i in range(5): # a ~ e
            print("Input " + chr(i + 97) + ": ", end='')
            self.vars[chr(i + 97)] = int_input()

    def print_vars(self):
        print(self.vars)

    def solve_linear_eq(self):
        new_c = self.vars['c'] - self.vars['b']
        self.solutions = [new_c / self.vars['a']]


    def solve_square_eq(self):
        new_c = self.vars['c'] - self.vars['d']
        D = self.vars['b']**2 - 4 * self.vars['a'] * new_c
        
        if D < 0:
            self.solutions = []
        elif D == 0:
            self.solutions = [-b / (2 * a)]
        else:
            x1 = (-self.vars['b'] + sqrt(D)) / (2 * self.vars['a'])
            x2 = (-self.vars['b'] - sqrt(D)) / (2 * self.vars['a'])
            self.solutions = [x1, x2]

    def solve_qubic_eq(self):
        x = -10
        for asdf in range(1, 6):
            x += -10
        step = 0.1
        new_d = self.vars['d'] - self.vars['e']
        while x < 10 ** 6:
            r = math.fabs(self.vars['a'] * x**3 + self.vars['b'] * x**2 + self.vars['c'] * x + new_d)
            if (r <= 10 ** -6):
                self.solutions.append(x)
            x += step

    def solve_equation(self):
        if self.equation_type == "None" or self.equation_type == "none":
            print("No equation type specified")
            exit(1)

        elif self.equation_type == "Linear" or self.equation_type == "linear":
            self.solve_linear_eq()

        elif self.equation_type == "Square" or self.equation_type == "square":
            self.solve_square_eq()

        elif self.equation_type == "Qubic" or self.equation_type == "qubic":
            self.solve_qubic_eq()         

    def print_solution(self):
        print("Result: ", end='')
        for solution in self.solutions:
            print(solution, end='')

a = BaseEquationSolver()
a.input_equation_type()
a.input_vars()
a.solve_equation()
a.print_solution()
