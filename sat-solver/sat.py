"""
SAT Solver
==========

m denote the number of clauses
n denote the number of variables

in_subset of length m which specifies the subset of
variables that are assigned the value true.

n-charaters string, ith character in the string corresponds
to the i th variable, '+' represents true, '-' represents false,
'.' means the variable does not appear.

Example:

x'+z = true
x+y'+z = true
x+y = true
x'+y' = true

-.+
+-+
++.
--.
"""
import numpy as np
import sys

def check(clauses, in_subset):
  """
   Check function identifies any assignments which satisfies
   all of the equations.
   This function takes linear time in the problem size.
  """
  is_product = True
  for x in clauses:
    is_sum = False
    for j, y in enumerate(in_subset):
      if x[j] == '+':
        is_sum = is_sum or y
      if x[j] == '-':
        is_sum = is_sum or not y
    is_product = is_product and is_sum
  return is_product

def sat(clauses):
  n = len(clauses)
  in_subset = np.full((n, 1), 0)
  while has_item(n, in_subset):
    if check(clauses, in_subset):
      return (True, in_subset.transpose())
  return (False, [])

def has_item(n, in_subset):
  i = n - 1
  while(in_subset[i]):
    i -= 1
    in_subset[i] = 0;
    if i == -1:
      return False
  in_subset[i] = 1
  return True

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print('USAGE: python sat.py <input_file>')
    exit(-1)
  with open(sys.argv[1]) as f:
    print(sat([l.strip() for l in f.readlines()]))
