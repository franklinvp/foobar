def maximum_flow_on_graph(entrances, exits, path):
    """
    This challenge was essentially, up to some formulation with
    bunnies and stuff, computing maximum flow on a graph with possibly 
    several entrances and several exits. In the problem they said that the maximum
    flow was going to be not larger than 2000000, which is a bit large.
    So, probably using just Ford-Fulkerson 
        (https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)
    was going to be too slow for their test cases
    since this has complexity O(E*f), where E is the number of edges and f the maximum flow.
    I didn't try using Ford-Fulkerson, though. Maybe it would have worked.
    Instead I used Dinic's algorithm
        (https://en.wikipedia.org/wiki/Dinic%27s_algorithm)
    after adding a single source and a single exist to the graph.
    This function computes the maximum flow on a graph using Dinic's algorithm.
    Numbering the vertices 0,1,...,n
        entrances = list of vertices from which the flow enters
        exits     = list of vertices from which the flow exits
        path      = Capacity (maximum flow per edge) matrix of size n x n.
    entrances and exits are supposed to be disjoint subsets of vertices.
    It assumes that the maximum flow is 2000000.
    The function returns the maximum total flow reaching exits.
    """
    N = len(path)
    s_row = (N+2)*[0]
    for i in entrances:
        s_row[i+1] = 2000000
    # Constructing the capacity matrix for a graph that is the given graph
    # plus a single source vertex 's' and a single target vertex 't' added.
    # The vertex 's' will be 0 and the vertex 't' will be N+1.
    path_with_s_and_t = []
    path_with_s_and_t.append(s_row)
    for i in range(N):
        row_i = [0]
        for j in range(N):
            row_i.append(path[i][j])
        if i in exits:
            row_i.append(2000000)
        else:
            row_i.append(0)
        path_with_s_and_t.append(row_i)
    path_with_s_and_t.append((N+2)*[0])
    # The flow per edge will be put in here.
    flow_matrix = [(N+2)*[0] for i in range(N+2)]
    flow = 0
    def level_graph_reaches_t():
        """
        This computes of the level graph.
        This is defined as the subgraph of the recidual graph
        in which we tag 's' as 1, and vertices reachable from 
        's' as the minimum distance from 's'.
        The recidual graph is defined as the graph with the same
        vertices as the original graph, but with edges being those
        edges of the original graph for which the current flow
        is not equal to the capacity of the edge.
        
        This function returns True if 't' can be reached from 's'
        in the level graph.
        """
        queue = []
        queue.append(0)
        global level
        level = (N+2) * [0]
        level[0] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(N+2):
                    if (flow_matrix[k][i] < path_with_s_and_t[k][i]) and (level[i] == 0):
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[N+1] > 0
    def blocking_flow_depth_first_search(flow_matrix, k, cp):
        """
        This function constructs a blocking flow starting from vertex k
        and maximum capacity cp.
        """
        tmp = cp
        if k == N+1:
            return cp
        for i in range(N+2):
            if (level[i] == level[k] + 1) \
                and (flow_matrix[k][i] < path_with_s_and_t[k][i]):
                f = blocking_flow_depth_first_search(flow_matrix, 
                                                     i, 
                                                     min(tmp, 
                                                         path_with_s_and_t[k][i] - flow_matrix[k][i]))
                flow_matrix[k][i] += f
                flow_matrix[i][k] -= f
                tmp = tmp - f
        return cp - tmp
    # Dinic algorithm.
    # While the level graph can get to 't' get a blocking flow
    # and add it to the current flow.
    while(level_graph_reaches_t()):
        flow += blocking_flow_depth_first_search(flow_matrix, 0, 2000000)
    return flow
