"""
 Coupon Collector

 Input: n
"""
import sys
import random

def coupon(n):
  sequence = [False] * n
  count = 0
  distinct = 0
  while(True):
    count += 1
    r = random.randint(0, n-1)
    if not sequence[r]:
      distinct += 1
      sequence[r] = True
    if distinct == n:
      return count
  # error
  return -1

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('USAGE\n python coupon <n> where n is number of coupon')
    exit(-1)

  n = int(sys.argv[1])
  print(coupon(n))
