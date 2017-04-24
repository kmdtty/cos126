"""
SQRT

Calculate the square root as an example of the iterative method.

Reference:
  http://mathworld.wolfram.com/NewtonsIteration.html
  https://en.wikipedia.org/wiki/Iterative_method
"""
import sys

def sqrt(number):
  """
    x^2     = c
    {divide by x}
    x       = c/x
    {move c/x from rhs to lhs}
    x - c/x = 0
  """
  epcilon = 1e-15 # 1*(10**-15)
  x = number
  while((x - number/x) > epcilon):
    x = (x + number/x)*0.5
  return x

if __name__ == '__main__':
  if len(sys.argv ) < 2:
    print("USAGE: python sqrt.py <a real number>")
    exit(-1)

  number = float(sys.argv[1])
  print(sqrt(number))
