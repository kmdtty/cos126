"""
INPUT: a Graph,
       a Delimter

OUTPUT:
|v|                       := number of verticies
|E|                       := number of edges
avg(Kv_i) = sum(Kv_i)/|v| := average degree
avg(shortestpath(edges))  := average path length
CC(g) = avg(lcc(v_i))     := clustering coefficient of the graph
      = sum(lcc(v_i))/|v|

lcc(v_i) = 2N_v/Kv_i(Kv_i -1) := local clustering coefficient at the vartex

def. Small Graph
----------------
- sparce (the average degree is < 20)
- short  (the average pathe length is < 10)
- locally (the clustering coefficient > 0.1)

Example:
--------

% python smallworld.py tinyGraph.txt " "
5 verticies, 7 edges
average degree  = 2.8
average path length = 1.3
clustering coefficient = 0.767
The graph is a small graph.
"""
if __name__ == '__main__':
  pass

