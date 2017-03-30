"""
Input
-----

Inputs represent a web pages graph.

= Syntax:

n
f_i t_i_j .. f_i t_i_n
..
f_n t_n_j .. f_n t_n_n

where f_i and t_i are integers between [0, n)

= Semantics

f_i is the from pages
t_i_j is the to pages lined from the page f_i
n is the number of from and to pair

Output
------

Transition matrix

= Def.
Transition matrix is a n square matrix which represents the probability of
the transition from a state i to a state j in a finite marcov chain.


= Assumtion of this transition:
- 90% of users click a link inside the current page
  with the uniform distribution
- 10% of users drectory move to a page inside the web with
  the uniform distribution

"""

import numpy as np

"""
1. link = caluculate link probability by each page
2. leap = calculate leap probability by each page
3. transition = link + leap
"""
n = 5
a = np.zeros((n, n))

def link_probability():
  pass

def leap_probability():
  pass

def transition():
  pass

