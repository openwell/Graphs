from util import Stack, Queue 


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
                 # set arranges the no add to it
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 and v2 exist in vertices list
        if v1 in self.vertices and v2 in self.vertices:
        # based on the way we are working we dont want anything to be reset
        # wasn't included in the original graph
            # add v2 at v1 of vertices
            # (add v2 to the vertices list at the index of v1)
            self.vertices[v1].add(v2)
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

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), 
# (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    newgraph = Graph()

    for i in range(len(ancestors)):
        data = ancestors[i]
        newgraph.add_vertex(data[0])
        newgraph.add_vertex(data[1])
        newgraph.add_edge(data[1], data[0])


    # if len(newgraph.vertices[starting_node]) < 1:
    #     return -1
    # q = Queue()
    # # we can make use of [] to view what we are working on
    #     # first in first out
    # q.enqueue(starting_node)
    #     # create a set to store the visited vertices
    # visited = set()
    # # while the queue is not empty
    # while q.size() > 0:
    #     # Dequeue the first vertex
    #     v = q.dequeue()
    #     # if that vertex has not been visited
    #     if v not in visited:
    #         # mark it as visited (printing for a representation)
    #         # print(v)
    #         visited.add(v)
    #         # then add all of it's neighbors to the back of the queue
    #         for next_vertex in newgraph.vertices[v]:
    #             q.enqueue(next_vertex)
    # return v

    q = Queue()
    # enqueue starting node inside a list
    q.enqueue([starting_node])
    # set a max path length to 1
    max_path_length = 1
    # set initial earlyest ancestor
    earliest_ancestor = -1
    # while queue has contents
    while q.size() > 0:
        # dequeue the path
        path = q.dequeue()
        # get the last vert
        vert = path[-1]
        # print(vert, len(path) >= max_path_length, vert < earliest_ancestor, len(path) > max_path_length)
        # if path is longer or equal and the value is smaller, or if the path is longer
        
        
        # the right side of the if is to start it.... the left is to end it
        # [1,3,6]
        #  3>=1      6< -1 
        #  2>=3      3>6
        #  1>=2      1<3
        if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest ancestor to the vert
            earliest_ancestor = vert
            # set the max path length to the len of the path
            max_path_length = len(path)
        # loop over each neighbor in the graphs vertices at index of vert
        for neighbor in newgraph.vertices[vert]:
            # make a copy of the path
            print(neighbor)
            path_copy = list(path)
            # append neighbor to the coppied path
            path_copy.append(neighbor)
            # then enqueue the copied path
            q.enqueue(path_copy)
    # return earliest ancestor
    return earliest_ancestor

        


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors , 8))
