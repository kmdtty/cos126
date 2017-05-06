"""
Three sum
---------

INPUT: random n sequence

OUTPUT: Count the triples whose sume is zero in the sequence

"""
import sys

def three_sum(array):
  n = len(array)
  count = 0
  triple_list = []
  for x in range(n) :
    for y in range(x+1, n):
      for z in range(y+1, n):
        if array[x] + array[y] + array[z] == 0:
          count += 1
          triple_list.append((array[x], array[y], array[z]))
  return count, triple_list

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('USAGE:\n python trhee_sum.py <array of numbers>')
    exit(-1)
  with open(sys.argv[1]) as f:
    array = [int(x.strip()) for x in f.readlines()]
    # array = f.split('\n')
    print(three_sum(array))
