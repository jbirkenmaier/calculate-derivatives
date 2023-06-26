import calculate_derivative as cd
import numpy as np
import math



formula = '2*x^(1/2)$+$'+cd.call_sum(1,2,'i*x^i', 'i')

print(cd.create_terms_from_string('1+2*(x^2)*x^3'))

coeff_power = cd.interprete_string_formula(formula, 'x')

derivative = cd.poly_deriv(coeff_power)

for i in range(len(coeff_power)):
    if i != len(coeff_power)-1:
        print(str(derivative[i].coefficient) +  'x^' + str(derivative[i].power) + '+', end = '\r')
    else:
        print(str(derivative[i].coefficient) +  'x^' + str(derivative[i].power))
