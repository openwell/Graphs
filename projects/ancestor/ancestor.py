from util import Stack, Queue 


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 and v2 exist in vertices list
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 at v1 of vertices
            # (add v2 to the vertices list at the index of v1)
            self.vertices[v2].add(v1)
        # otherwise
        else:
            # raise an error
            raise KeyError("That vertex does not exist", v1, v2)
# set ()   or countries = {'nigeria', 'kenya', 'congo'}
# dic {}
# list []
# tuple
# []list  ()tuple {}set {k=u} dictionary
# tuple(('lemon', 'eggs', 'pawpaw'))

def earliest_ancestor(ancestors, starting_node):
    newgraph = Graph()

    for i in range(len(ancestors)):
    #    print(ancestors[i][0])
        data = ancestors[i]
        newgraph.add_vertex(data[0])
        newgraph.add_vertex(data[1])
        # if [1] is in any of the vertics then add it to its set
    for i in range(len(ancestors)):
        v1 = ancestors[i][0]
        v2 = ancestors[i][1]
        newgraph.add_edge(v1, v2)

    # print(newgraph.vertices)
    # for i in newgraph.vertices:
    if len(newgraph.vertices[starting_node]) < 1:
        return -1

    q = []
        # first in first out
    q.append(starting_node)
        # create a set to store the visited vertices
    visited = set()
    # while the queue is not empty
    while len(q) > 0:
        # Dequeue the first vertex
        v = q.pop(0)
        # if that vertex has not been visited
        if v not in visited:
            # mark it as visited (printing for a representation)
            # print(v)
            visited.add(v)
            # then add all of it's neighbors to the back of the queue
            for next_vertex in newgraph.vertices[v]:
                q.append(next_vertex)
    return v

        


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors , 7))
