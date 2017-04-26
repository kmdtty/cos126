"""
Sampling
--------

Sample random m integers in range [0, n-1].

"""
import sys
import random

def sample(m, n):
  sequence = [x for x in range(n)]
  for i in range(m):
    r = random.randint(0, n-1)
    sequence[i] = sequence[r]
    sequence[r] = i
  return sequence[0:m]

if __name__ == '__main__':
  if len(sys.argv)  != 3:
    print('USAGE\n % python sample.py <m> <n>')
    print(' where m is required length of random integers, n is the integer range')
    exit(-1)
  m = int(sys.argv[1])
  n = int(sys.argv[2])
  print(sample(m, n))
