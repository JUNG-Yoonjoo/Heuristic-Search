#!/usr/bin/env python
# coding: utf-8

# In[21]:


from __future__ import print_function

from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

variables = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

domains = dict((v, ['1', '2', '3']) for v in variables)

def const_different(variables, values):
    return values[0] != values[1]

constraints = [
    (('A', 'B'), const_different),
    (('B', 'C'), const_different),
    (('C', 'D'), const_different),
    (('D', 'E'), const_different),
    (('E', 'F'), const_different),
    (('A', 'F'), const_different),
    (('A', 'C'), const_different),
    (('D', 'F'), const_different),
    (('C', 'G'), const_different),
    (('D', 'G'), const_different),
    (('F', 'H'), const_different),
    (('A', 'H'), const_different),
]

my_problem = CspProblem(variables, domains, constraints)

print(backtrack(my_problem))

print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))

print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))

print(backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE))

print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))

print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))

print(min_conflicts(my_problem))


# In[ ]:




