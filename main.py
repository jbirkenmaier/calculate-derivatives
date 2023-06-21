import calculate_derivative as cd
import numpy as np
import math



formula = '2*x^0$+$'+cd.call_sum(1,2,'i*x^i', 'i')

coeff_power = cd.interprete_string_formula(formula, 'x')

for i in range(len(coeff_power)):
    print(str(cd.poly_deriv(coeff_power)[i].coefficient) +  'x^' + str(cd.poly_deriv(coeff_power)[i].power))


