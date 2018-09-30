"""
Just an example of a didactic graph class, mainly to do Depth First Search (DFS)
and Breadth First Search (BFS).
"""

from collections import deque

class Graph:
    """
    The graph will be modeled using an adjacency.
    More specifically, with a dictionary (has table) of the vertices
    asociating to each a list of its neighbours.
    The constructor can be passed such dictionary, if wanted.
    """
    def __init__(self, adjacency_list = None):
        if adjacency_list == None:
            adjacency_list = {}
        self.adjacency_list = adjacency_list
        # The following will be used by the DFS.
        self.colors = {}
        self.predecessor = {}
        self.f_times = {}
        self.d_times = {}
        self.time = 1

    def vertices(self):
        return self.adjacency_list.keys()

    def edges(self):
        return self._generate_edges()

    def add_vertex(self, vertex):
        """
        No change if the vertex is already here.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = deque()

    def add_edge(self, edge):
        """
        edge is input as a pair, of list with two elements,
        or tuple.
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
        else:
            self.adjacency_list[vertex1] = deque()
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = deque()

    def _generate_edges(self):
        """
        This list could be stored, and computed only if we know 
        that the graph has been modified.
        """
        return  [(vertex, neighbour) \
                 for vertex in self.adjacency_list \
                 for neighbour in self.adjacency_list[vertex]]
                 
    def __str__(self):
        res = ["vertices: "]
        for k in self.adjacency_list:
            res += [str(k.value), ", "]
        res += ["\nedges: "]
        for edge in self._generate_edges():
            res += [str(edge), ", "]
        return "".join(res)

    def DFS(self, start, fresh_run = True):
        """
        DFS will compute 4 functions of the vertices of the 
        connected component of start:
            * colors: All the vertices of the connected component
                      will be 'black'. Those that can't be reached 
                      from start will be 'white'.
            * predecessor: Indicates the vertex from which the vertex
                           was reached during the DFS.
            * d_times: The time (DFS turn) in which the vertex was 
                       discovered.
            * f_times: The time (DFS turn) at which the all vertex's 
                       neighbours were finally found.
        DFS can be made to visit all vertices in the graph. But this 
        DFS only visits the connected component.
        
        This implementation is iterative, instead of the easier to 
        read recursive one.
        
        fresh_run can be set to False if one wants to run the method 
        with other start vertices, while preserving the color, predecessor, 
        d_times, and f_times already computed.
        """
        if start in self.adjacency_list:
            if fresh_run:
                self.colors = {key:'white' for key in self.adjacency_list.keys()}
                self.predecessor = {key:None for key in self.adjacency_list.keys()}
                self.f_times = {key:0 for key in self.adjacency_list.keys()}
                self.d_times = {key:0 for key in self.adjacency_list.keys()}
                self.time = 1
            # This deque will be used as a stack.
            # Vertices contained in to_finish were discovered, but their
            # neighbours still need to be explored to see if there are 
            # undiscovered ('white') among them.
            to_finish = deque()
            self.d_times[start] = time
            self.colors[start] = 'gray'
            to_finish.append(start)
            while to_finish:
                w = to_finish.pop()
                # Let's see if some neighbour of w hasn't been visited.
                has_unvisited_neighbours = False
                for s in self.adjacency_list[w]:
                    if self.colors[s] == 'white':
                        has_unvisited_neighbours = True
                        break
                # Take into account that in Python the loop variable
                # will still exist and retain its last value after
                # exiting the loop. We will use it. In other languages
                # the variable s might need to be declared in this scope,
                # outside the loop.
                if not has_unvisited_neighbours:
                    # The vertex w is done. Marking it as 'black'
                    # and recording its finishing time.
                    self.colors[w] = 'black'
                    self.time += 1
                    self.f_times[w] = self.time
                else:
                    # New vertex s found. Marking s as 'gray',
                    # recording its discovery time, putting w back
                    # in the stack because it might still have more
                    # undiscovered neighbours. The vertex s will also
                    # go into the stack, but notice that it goes after w
                    # in this way s gets to be processed further before w.
                    # This is why the algorithm is called Depth First Search.
                    self.predecessor[s] = w
                    to_finish.append(w)
                    self.time += 1
                    self.d_times[s] = self.time
                    self.colors[s] = 'gray'
                    to_finish.append(s)
            return self.predecessor, self.d_times, self.f_times, self.colors
