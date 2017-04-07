"""
Transition matrix

= Def.
Transition matrix is a n square matrix which represents the probability of
the transition from a state i to a state j in a finite marcov chain.

= Assumtion of this transition:
- 90% of users click a link inside the current page
  with the uniform distribution
- 10% of users drectory move to a page inside the web with
  the uniform distribution

Input
-----

Inputs represent a web pages graph.

= Syntax:

n
f_i t_i_j .. f_i t_i_n
..
f_n t_n_j .. f_n t_n_n

where f_i and t_i_j are integers between [0, n)

= Semantics

f_i is the from pages
t_i_j is the to pages linked from the page f_i
n is the number of pages

"""

import numpy as np
from collections import defaultdict
from collections import Counter
import sys

def transition(filename):
  """
    1. link = (.9/number of links in the page) * number of links to the page
    2. leap = .1/n
    3. transition_matrix = link + leap
  """
  with open(filename, 'r') as g:
    link_counter = Counter()
    page_counter = Counter()
    # Head-Tail pattern
    g_iter = iter(g)
    n = int(next(g_iter, 0))
    transition_matrix = np.zeros((n, n))
    for line in (l.strip() for l in g_iter if l.strip()):
      pair_list = line.split('  ')
      for pair in pair_list:
        source, destination = [int(p) for p in pair.split(' ')]
        page_counter.update([(source, destination)])
        link_counter.update([source])
    for s, d in page_counter.elements():
      transition_matrix[s][d] = (.9 / link_counter[s]) * page_counter[(s, d)] + .1/n
    return transition_matrix

def main():
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    print('USAGE:\n python transition.py <graph_data_file>')
    exit(-1)
  print(transition(filename))

if __name__ == "__main__":
  main()
