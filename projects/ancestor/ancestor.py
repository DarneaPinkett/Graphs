from util import Queue

'''
start w/ making Queue
Enqueue list w/ starting node
start w/ empty list of ancestors
make empty visited set

while queue is not empty
dequeuw list in
look at parent(1st element) in dequeue tuple
see if parent has been visited, mark as visited
check if one is longer than the rest

'''

class Graph:
    
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
        
    q = Queue()
    q.enqueue([starting_node])

    longest_path = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if (len(path) >= longest_path and v < earliest_ancestor) or (len(path) > longest_path):
            earliest_ancestor = v
            longest_path = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor