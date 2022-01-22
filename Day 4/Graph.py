class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    
    def get_vertices(self):
        return list(self.gdict.keys())

    def get_edges(self):
        edges = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex, vertex} not in edges:
                    edges.append({vertex, next_vertex})
        return edges

    def edges(self):
        return self.get_edges()
    
    def add_vertex(self,vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
    
    def add_edges(self, edge):
      edge = set(edge)
      (vertex1, vertex2) = tuple(edge)
      if vertex1 in self.gdict:
         self.gdict[vertex1].append(vertex2)
      else:
         self.gdict[vertex1] = [vertex2]

vertex = ['a', 'b', 'c', 'd', 'e']
edges = ['ab', 'ac', 'bd', 'cd', 'de']
graph_elements = {}
for i in vertex:
    graph_elements[i] = []
    for j in edges:
        if (str(i) == str(j[0])):
            graph_elements[i].append(j[-1])
for i in vertex:
    if (graph_elements[i] == []):
        del graph_elements[i]
print(graph_elements)
g = graph(graph_elements)
print(g.get_vertices())
print(g.get_edges())
g.add_vertex("e")
g.add_vertex("f")
print(g.get_vertices())
g.add_edges({'e','a'})
g.add_edges({'f','b'})
print(g.get_edges())
for i in g.get_vertices():
    if (graph_elements[i] == []):
        del graph_elements[i]
print(graph_elements)