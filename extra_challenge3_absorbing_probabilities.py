def absorbing_probabilities(m):
    """
    This was not one of the challenges made to me.
    In particular it hasn't been tested against 
    the secret test cases.
    
    Given the transition probabilities matrix m
    of a random walk on a graph, this function computes 
    the absorbing probabilities. This is, the probabilities 
    to reach the absorving nodes.

    The matrix is assumed to be of non-negative integer 
    entries. The probabilities are the entries divided by
    the sum of the elements of the corresponding row.

    The initial state corresponds to the first row.

    The output is a list contaning first all the numerators
    of the probabilities of the absorving nodes, and the last
    entry is the common denominator.
    """
    # Some basic functions to compute with fractions.
    # The fractions are modeled as pairs of int.
    # This is for a small and self-contained example.
    # If wanted one can define a fraction type, and
    # overloading operators the code for LU will look nicer.
    def gcd(a, b):
        # Implement or load from 
        # from fractions import gcd
        while b:
            a, b = b, a%b
        return a
    def lcd(a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        return (a*b)//gcd(a,b)
    def simplify_fraction(x):
        if not x[1] == 0:
            g = gcd(x[0],x[1])
            if not g == 0 and not g == 1:
                return [x[0] // g, x[1] // g]
        return x
    def sum_fractions(x,y):
        return [x[0]*y[1]+x[1]*y[0], x[1]*y[1]]
    def subtract_fractions(x,y):
        return [x[0]*y[1]-x[1]*y[0], x[1]*y[1]]
    def multiply_fractions(x,y):
        return [x[0]*y[0],x[1]*y[1]]
    def divide_fractions(x,y):
        return [x[0]*y[1],x[1]*y[0]]
    def gt_fractions(x,y):
        return x[0]*y[1] > y[0]*x[1]
    def abs_fractions(x):
        return [abs(x[0]), abs(x[1])]
    def LU_solve(A,b):
        # Here I assume that each row of b
        # is a 'column' vector c for which one 
        # wants to solve Ax = c.
        #
        # Computing LU factorization of A
        n = len(A)
        P = [i for i in range(n)]
        for i in range(n):
            maxA = [0,1] # fraction 0/1
            imax = i
            for k in range(i,n):
                absA = abs_fractions(A[k][i])
                if gt_fractions(absA,maxA):
                    maxA = absA
                    imax = k
            if maxA[0] == 0:
                return b, False
            if not imax == i:
                j = P[i]
                P[i] = P[imax]
                P[imax] = j
                ptr = A[i]
                A[i] = A[imax]
                A[imax] = ptr
                P[n] += 1
            for j in range(i+1,n):
                A[j][i] = divide_fractions(A[j][i], A[i][i])
                for k in range(i+1,n):
                    A[j][k] = subtract_fractions(A[j][k],multiply_fractions(A[j][i],A[i][k]))
        # Solving Ax = c for each row c of b, interpreted as a column vector.
        for c in range(len(b)):
            x = [[0,1] for i in range(n)]
            for i in range(n):
                x[i] = b[c][P[i]]
                for k in range(i):
                    x[i] = subtract_fractions(x[i], multiply_fractions(A[i][k],x[k]))
            for i in range(n-1,-1, -1):
                for k in range(i+1,n):
                    x[i] = subtract_fractions(x[i],multiply_fractions(A[i][k],x[k]))
                x[i] = divide_fractions(x[i], A[i][i])
            b[c] = x
        return b
    # Now the actual computation
    #
    number_nodes = len(m)
    # These are to turn the entries of the input
    # into probabilities.
    denominators = [sum(x) for x in m]
    # The initial state might be a terminal state in principle.
    # If so, there is nothing to compute. The output is [1,0,...,0,1]
    if denominators[0] == 0:
        return [1] + (number_nodes-1)*[0] + [1]
    # This is the list of Terminal nodes. 
    terminal_nodes = [i+1 for i in range(number_nodes-1) if denominators[i+1] == 0]
    # Transient nodes are the states from which you could 
    # transform to other states.
    transient_nodes = [i for i in range(number_nodes) if i not in terminal_nodes]
    # I - Transient matrix. 
    # The Transient matrix is the matrix of transition probabilities
    # to get from transient states to transient states.
    I_minus_Q = [[simplify_fraction([-m[i][j],denominators[i]]) \
        if not i == j else simplify_fraction([denominators[i]-m[i][j],denominators[i]]) \
        for j in transient_nodes] for i in transient_nodes]
    # Transient to terminal matrix transposed.
    # This is, the matrix of trasition probabilities to get from transient
    # states to terminal states. 
    # Here I put the matrix transposed for convenience when inputing it 
    # into LU_solve(...)
    R = [[simplify_fraction([m[i][j],denominators[i]]) \
        for i in transient_nodes] for j in terminal_nodes]
    solution = LU_solve(I_minus_Q, R)
    # Simplyfying fraction of the result.
    # Maybe one can add some simplify_fraction while
    # doing the LU and/or the back/forth substitutions
    # too, if one wants to keep the intermediate values small.
    for i, elem in enumerate(solution):
        # We only need the first column
        solution[i] = simplify_fraction(elem[0])
    overall_lcd = 1
    output = []
    # Getting the least common denominator
    # for the probabilities that we need to output.
    for i in solution:
        if not i[0] == 0:
            overall_lcd = lcd(overall_lcd,i[1])
    for i in solution:
        output += [i[0]*overall_lcd//i[1]]
    output += [overall_lcd]
    return output
