"""
Computes all permutations of {1,2,...,n-1}.

Permutohedron: Vertices are permutations
               Edges between vertices that are different by a transposition of consecutive indices.

It turns out that the permutohedron has Hamiltonian cycles.
Steinhaus-Johnson-Trotter-Even's algorithm travels one such Hamiltonian cyle of the permutohedron.
"""

def _visit(L):
    """
    Whatever one needs to do with the current permutation (without altering it).
    For example, printing it.
    """
    print(L)

def steinhaus_johnson_trotter_even(n):
    L = [i+1 for i in range(n)]
    _visit(L) # or whatever one needs to do with the current permutation
    directions = n*[-1] # -1 means could move to the left, 1 means could move to the right, 0 means stay put.
    directions[0] = 0
    # The largest element with non-zero direction is the last one.
    to_move = n-1
    while to_move:
        # Position to which the to_move will be moved.
        other = to_move + directions[to_move]
        if other < n and other >= 0:
            # If the new position is inside the transposition is applied.
            L[other], L[to_move] = L[to_move], L[other]
            # The same transposition applied to the list of directions.
            directions[other], directions[to_move] = directions[to_move], directions[other]
            _visit(L) # or whatever one needs to do with the current permutation
            # Position to which to_move would be if continuing in the same direction.
            one_more = other + directions[other]
            if other == 0 or other == n-1 \
               or (one_more < n and one_more >= 0 and L[one_more] > L[other]):
                directions[other] = 0
            # Larger elements than the one moved get direction +1 if they are on the left of it
            # and -1 if they are on the right.
            for i in range(n):
                if L[i] > L[other]:
                    if i < other:
                        directions[i] = 1
                    elif i > other:
                        directions[i] = -1
        # Finding the largest element with non-zero direction.
        # This becomes the next element to get moved.
        to_move = None
        max = -1
        for i in range(n):
            if directions[i] != 0 and L[i] > max:
                max = L[i]
                to_move = i
