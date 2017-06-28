"""
Pagerank
========

1. Random surfer model is a Markov chain
2. Markov chain converge the same probability no matter where it starts.
3. Calculate from [1 0 0 ... ] * [transition matrix]
4. Calculate k times
"""

from transition import transition
import numpy as np
import sys

K = 100

def pagerank(filename):
  transition_matrix = transition(filename)
  n = transition_matrix.shape[0]
  v = np.zeros((1, n))
  v[0,0] = 1.0
  vm = v.dot(transition_matrix)
  for _ in range(K-1):
    vm = vm.dot(transition_matrix)
  print(vm)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    filename = sys.argv[1]
    pagerank(filename)
  else:
    print('USAGE:\n python pagerank <network graph file>')
