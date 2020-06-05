from collections import Counter

def buildGCDTable(n):
    """
    Build the gcd table for all pairs (x,y) with x,y <= n.
    """
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i == 0 or j == 0:
                result[i][j] = 1
                result[j][i] = 1
            elif i == j:
                result[i][j] = i+1
            else:
                result[i][j] = result[i][j-i-1]
                result[j][i] = result[i][j-i-1]
    return result

def gcd(x,y, gcdTable):
    """
    Because we are going to need the gcd of many pairs of numbers
    we compute the full gcd table of the numbers that we need, instead 
    of applying Euclid's algorithm for each pair.
    Note that Euclid's algorithm essentially computes, for large inputs, the gcd
    of many smaller values too. Since we need them all, we compute them
    bottom up, as in Dynamic Programming.
    """
    return gcdTable[x-1][y-1]

def buildFactorialTable(n):
    """
    Build the factorials of all the numbers 1,2,3,...,n
    We will need them all. So, lets compute them also
    bottom up, as in Dynamic Programming.
    """
    result = [1]
    for i in range(n-1):
        result.append(result[-1]*(i+2))
    return result

def factorial(x, factorialTable):
    """
    Read from the pre-computed table.
    """
    return factorialTable[x-1]

def coefficientFactor(c, n,factorialTable):
    """
    Computes 
    
        n!/(1^{i_1}i_1!2^{i_2}i_2!...n^{i_n}i_n!)

    where c is a partition of n that has 
    i_1 1s, i_2 2s, ..., and i_n ns.
    """
    cc=factorial(n,factorialTable)
    for a, b in Counter(c).items():
        cc//=(a**b)*factorial(b,factorialTable)
    return cc

def partitionsAndCycleCount(n,factorialTable):
    """
    Iterative algorithm to generate all partitions of 
    the positive integer n.
    In addition to each partition, we compute the following number:
        if the partition has i_1 1s, i_2 2s, ..., i_n ns, we compute
        n!/(1^{i_1}i_1!2^{i_2}i_2!...n^{i_n}i_n!)
    """
    k = 0  # Index of last element in a partition 
    p = n*[0] # To store a partition in p[0:k+1]
    p[0] = n  # First partition is [n]
    result = [] # To store all partitions
    # The loop stops when the current partition has all 1s 
    while True:
        # Add current partition to the result
        result.append((p[0:k+1],coefficientFactor(p[0:k+1],n,factorialTable)))
        ## Generate next partition 
        # Find the rightmost non-one value in p[]. 
        # Update rem_val so that we know how much value can be accommodated 
        rem_val = 0
        while k >= 0 and p[k] == 1:
            rem_val += p[k]
            k -= 1
        # if k < 0, all the values are 1 so there are no more partitions 
        if k < 0:
            return result
        # Decrease the p[k] found above and adjust the rem_val 
        p[k] -= 1 
        rem_val += 1
        # If rem_val is more, then the sorted order is violated.  Divide 
        # rem_val in different values of size p[k] and copy these values at 
        # different positions after p[k] 
        while rem_val > p[k]:
            p[k+1] = p[k]
            rem_val -= p[k]
            k += 1 
        # Copy rem_val to next position and increment position 
        p[k+1] = rem_val
        k += 1

def solution(w, h, s):
    # We are going to need the gcd for all pairs of numbers (a,b)
    # with a<= w and b <= h. So, let's compute them all.
    n = max(w,h)
    gcdTable = buildGCDTable(n)
    # We will also need the factorials of all numbers 1,2,...,max(w,h)
    factorialTable = buildFactorialTable(n)
    # Consider G=S_w\times S_h, acting on X=W\times H, where 
    # W={1,2,...,w}, H={1,2,...,h}, S_w and S_h are the symmetric group
    # acting as permutations of W and H, respectively.
    # Each matrix is a function f\in S^X, f:X to S, where 
    # S={1,2,...,s}.
    # G acts on S^X, by (gf)(x)=f(gx) for g\in G and f\in S^X.
    # We need to compute the orbits of G in S^X.
    # Polya's enumeration theorem, tell us how to obtain it 
    # from the Cycle Index Polynomial of the group action.
    # See https://franklinvp.github.io/2020-06-05-PolyaFooBar/
    # for the formula.
    grid=0
    for cpw in partitionsAndCycleCount(w,factorialTable):
        for cph in partitionsAndCycleCount(h,factorialTable):
            m=cpw[1]*cph[1]
            grid+=m*(s**sum([sum([gcd(i, j, gcdTable) for i in cpw[0]]) for j in cph[0]]))
    return str(grid//(factorial(w,factorialTable)*factorial(h,factorialTable)))

