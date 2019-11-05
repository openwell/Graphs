"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


    # COMPARISON	STACK	                     QUEUE
# Working principle	LIFO (Last in First out)	FIFO (First in First out)
# Structure	Same end is used to insert and delete elements.	One end is used for insertion, i.e., rear end and another end is used for deletion of elements, i.e., front end.
# Number of pointers used	One	                Two (In simple queue case)
# Operations performed	Push and Pop	        Enqueue and dequeue
# Examination of empty condition	Top == -1	Front == -1 || Front == Rear + 1
# Examination of full condition
# Top == Max - 1	                            Rear == Max - 1
# Variants	It does not have variants.	        It has variants like circular queue, priority queue, doubly ended queue.
# Implementation	                            Simpler	Comparatively complex

# Breadth-First Search ( or Traversal) also know as Level Order Traversal.
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
            self.vertices[v1].add(v2)
        # otherwise
        else:
            # raise an error
            raise KeyError("That vertex does not exist")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        # first in first out
        q.enqueue(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        # Last in last out
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited (printing for a representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)
            # it push watever that is inside it and works with the stack
            # then as it moves from one point to another the stacks add to itself
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # the stack was eliminated because visited was ok 
        # and since we are working on the whatever we get immediately
        # if not starting_vertex:
        #     return
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for i in self.vertices[starting_vertex]:
            if i not in visited:
              self.dft_recursive(i, visited)
    



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # vertices = self.vertices
        # # maintain a queue of paths
        # queue = []
        # # push the first path into the queue
        # queue.append([starting_vertex])
        # while len(queue) > 0:
        #     # get the first path from the queue
        #     print(queue)
        #     path = queue.pop(0)
        #     print(queue)
        #     # get the last node from the path
        #     node = path[-1]
        #     # path found
        #     if node == destination_vertex:
        #         return print(path)
        #     # enumerate all adjacent nodes, construct a new path and push it into the queue
        #     for adjacent in verts.get(node, []):
        #         new_path = list(path)
        #         new_path.append(adjacent)
        #         queue.append(new_path)  
        #         verts = self.vertices


        # maintain a queue of paths
        queue = Queue()
        # push the first path into the queue
        queue.enqueue([starting_vertex])
        # forget about everything up from here
        while queue.size() > 0:
            # get the first path from the queue
            path = queue.dequeue()
            # major code hold the previous path ..then the other adds to it
            # get the last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return print(path)
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for i in self.vertices.get(node):
                new_path = list(path)
                new_path.append(i)
                queue.enqueue(new_path)  


        # q = Queue()
        # # FIFO
        # q.enqueue(starting_vertex)
        # # create a set to store the visited vertices
        # visited = set()
        # path = {}
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
        #         for next_vertex in self.vertices[v]:
        #             q.enqueue(next_vertex)
                    


    def dfs(self, starting_vertex, destination_vertex):
        """
        Dijkstra's shortest path
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))



