"""
Given a graph G = (V, E), three functions of vertices will be computed:
    - predecessor
    - discorvery time
    - finished (processing) time
Three colors (marks on vertices) will be used:
    - white = not visited
    - gray = visited but not done yet dicovering its successors
    - black = done discovering its successors.
"""

# Recursive
def DFS(G):
    for u in G.vertices:
        u.color = 'white'
        u.predecessor = None
    time = 0
    for u in G.vertices:
        if u.color == 'white':
            DFS_VISIT(u, time)

def DFS_VISIT(u, time):
    u.color = 'gray'
    time += 1
    u.d_time = time
    for v in u.neighbours:
        if v.color == 'white':
            v.predecessor = u
            DFS_VISIT(v)
    u.color = 'black'
    time += 1
    u.f_time = time


# Iterative
def DFS_ITERATIVE(G):
    for v in G.vertices:
        v.color = 'white'
        v.predecessor = None
    to_finish = deque()
    for v in G.vertices:
        time = 0
        if v.color == 'white':
            time += 1
            v.d_time = time
            to_finish.append(v)
        while to_finish:
            w = to_finish.pop()
            has_unvisited_sucessor = False
            for s in w.neighbours:
                if s.color == 'white':
                    has_unvisited_successor = True
                    break
            if not has_unvisited_successor:
                w.color = 'black'
                time += 1
                w.f_time = time
            else:
                s.predecessor = w
                to_finish.append(w)
                time += 1
                s.d_time = time
                to_finish.append(s)
