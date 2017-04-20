"""
SAT Solver
==========

m denote the number of clauses
n denote the number of variables

bit_vector of length m which specifies the subset of
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

def check(clauses, bit_vector):
  """
   Check the candidate solution which is expressed as bit vector.
   This function takes linear time in the problem size.
  """
  sat_all_clause = True
  for clause in clauses:
    is_sat_a_clause = False
    for j, literal in enumerate(bit_vector):
      if clause[j] == '+':
        is_sat_a_clause = is_sat_a_clause or literal
      if clause[j] == '-':
        is_sat_a_clause = is_sat_a_clause or not literal
    sat_all_clause = sat_all_clause and is_sat_a_clause
  return sat_all_clause

def sat(clauses):
  n = len(clauses)
  bit_vector = np.full((n, 1), 0)
  while next_count(n, bit_vector):
    if check(clauses, bit_vector):
      return (True, bit_vector.transpose())
  return (False, [])

def next_count(n, bit_vector):
  """
   Count up the bit bector.

   Example:
   0 0 0 0
   0 0 0 1
   0 0 1 0
  """
  i = n - 1
  while(bit_vector[i]):
    i -= 1
    bit_vector[i] = 0;
    if i == -1:
      return False
  bit_vector[i] = 1
  return True

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print('USAGE: python sat.py <input_file>')
    exit(-1)
  with open(sys.argv[1]) as f:
    print(sat([l.strip() for l in f.readlines()]))
