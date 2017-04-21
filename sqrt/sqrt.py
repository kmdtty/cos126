"""
SQRT

Calculate the square root as an example of newton method.
"""
import sys

def sqrt(number):
  print(number)

if __name__ == '__main__':
  if len(sys.argv ) < 2:
    print("USAGE: python sqrt.py <a real number>")
    exit(-1)

  number = sys.argv[1]
  sqrt(number)
