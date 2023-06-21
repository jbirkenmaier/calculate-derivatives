import calculate_derivative as cd
import numpy as np
import math



formula = '2*x^0$+$'+cd.call_sum(0,2,'i*x^i', 'i')

print(cd.interprete_string_formula(formula, 'x'))
