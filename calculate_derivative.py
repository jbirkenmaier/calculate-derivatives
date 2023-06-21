import numpy as np


class poly_term:
    def __init__(self, variable, power, coefficient):
        self.variable = variable
        self.power=power
        self.coefficient=coefficient
        self.term = str(self.coefficient)+ '*' + self.variable + '^' + self.power

def sum_function_caller(function, index_name, index_value):
    return function.replace(index_name,str(index_value))

def call_sum(start, stop, function, ind_name):
    result = ''
    running_index=start
    while running_index<=stop:
        result += sum_function_caller(function, ind_name, running_index) + '$+$'
        running_index+=1
    return result[:-1]

#we have to interprete the string output of our "call_sum" function
def interprete_string_formula(str_formula, variable_name):
    terms = str_formula.split('$+$')
    coefficients = [element.partition(variable_name)[0] for element in terms]
    coefficients = [float(eval(element[:-1])) for element in coefficients]
    powers = [element.partition(variable_name)[2] for element in terms]
    powers = [float(element.replace('^', '').replace('+', '').replace('$','')) for element in powers]
    return coefficients, powers
    

#this function is supposed to create class objects of class poly_term which take input for example created by
#'interprete_string_formula' function. This is necessary to work with these objects in the future.

#def create_poly_terms:
#    pass

    

#to calculate the polynomial derivative I guess it is useful to read the polynomial as a string, then
#to interprete every term of the polynomial as an element of a class with coefficient and exponent.
#Then we can calculate the derivative easily for every element of the class, meaning for any term


def initialize_poly_term(coefficient, power, variable):
    pass
    
    


def deriv_poly(coeffs_powers, variable):
    #function is given in the format: [[coefficient, exponent of x]]

    coefficient_list= coeffs_powers[0]
    power_list = coeffs_powers[1]

    power_list = [element - 1 for element in power_list]
    coefficient_list = [power_list[i]*coefficient_list[i] for i in range(len(power_list))]

    return coefficient_list, power_list
    
#ISSUE: x^0 abgeleitet ist nicht x^-1
