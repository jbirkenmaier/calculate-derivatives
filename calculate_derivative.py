import numpy as np


class poly_term:
    def __init__(self, variable, power, coefficient):
        self.variable = variable
        self.power=float(power)
        self.coefficient=float(coefficient)

        self.power_str = str(self.power)
        self.coefficient_str = str(self.coefficient)
        self.term = str(self.coefficient_str)+ '*' + self.variable + '^' + self.power_str

def sum_function_caller(function, index_name, index_value):
    return function.replace(index_name,str(index_value))

def call_sum(start, stop, function, ind_name):
    result = ''
    running_index=start
    while running_index<=stop:
        result += sum_function_caller(function, ind_name, running_index) + '$+$'
        running_index+=1
    return result[:-1]

def interprete_string_formula(str_formula, variable_name):
    poly_terms=[]
    terms = str_formula.split('$+$')
    coefficients = [element.partition(variable_name)[0] for element in terms]
    coefficients = [float(eval(element[:-1])) for element in coefficients]
    powers = [element.partition(variable_name)[2] for element in terms]
    powers = [float(element.replace('^', '').replace('+', '').replace('$','')) for element in powers]
    for i in range(len(coefficients)):
        poly_terms.append(poly_term(variable_name, powers[i], coefficients[i]))
    return poly_terms

def poly_deriv(poly_attributes):
    for element in poly_attributes:
        if element.power == 0:
            element.coefficient = 0
        else:
            element.coefficient = element.coefficient*element.power
            element.power -=1
    return poly_attributes
        
    

