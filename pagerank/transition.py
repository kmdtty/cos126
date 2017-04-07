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
from collections import defaultdict
from collections import Counter
import sys

"""
1. link = 0.9/#number of links
2. leap = 0.1/n
3. transition = link + leap
"""
#a = np.zeros((n, n))

def link_probability():
  pass


def make_graph_matrix(filename):
  with open(filename, 'r') as g:
    counter = Counter()
    leap_matrix = None
    link_matrix = None
    n = None
    for i, line in enumerate(g):
      if i == 0:
        n = int(line.strip())
        leap_matrix = np.full((n, n), 0.1/n)
        link_matrix = np.zeros((n, n))
        continue
      data_line = line.strip()
      if not data_line:
        break
      pair_list = data_line.split('  ')
      link_dict = defaultdict(int)
      for pair in pair_list:
        source, destination = pair.split(' ')
        counter.update([(int(source), int(destination))])
    # FIXME: link probability calculation is wrong
    print(counter)
    for s, d in counter.elements():
      link_matrix[s][d] = 0.9 / counter[(s, d)]
    print(link_matrix)

def transition():
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    print('USAGE:\n python transition.py <graph_data_file>')
    exit(-1)
  g_matrix = make_graph_matrix(filename)

if __name__ == "__main__":
  transition()
