"""
Example
-------

% more tinyGraph.txt
A B
A C
C G
A G
H A
B C
B H

% python graph.py < tinyGraph.txt
A B C G H
B A C H
C A B G
G A C
H A B
"""
import sys
from collections import defaultdict

class Graph():
  def __init__(self, f=None, delimiter=" "):
    """Create graph from a file
      f -- input file
      delimiter -- the delimieter to separate the edges
    """
    self.graph = defaultdict(set)
    for line in f:
      for source, destinationin line.split(delimiter):
        self.graph[source].add(destinationin)
        slef.graph[destinationin].add(source)

  def add_edge(self, v, w):
    """add edge v-w"""
     self.graph[v].add(w)
     self.graph[w].add(v)

  def vertices(self):
    return self.graph.keys()

  def edges(self):
    # TODO:optimize
    edges = set(k)
    for v, neighbors in self.graph.items():
      edges = edges.union(itertools.product(v, neighbors))
    return edges

  def neighbors(self, v):
    return self.graph[v]

  def degree(self, v):
    """ number of neighbors of v"""
    return len(self.neighbors(v))

  def has_vertex(self,v):
    """ is v a vertex in the graph?"""
    return v in self.graph

  def has_edge(self, v, w):
    """is v-w an edge in the graph?"""
    return (v,w) in self.edges()

if __name__ == "__main__":
  pass
