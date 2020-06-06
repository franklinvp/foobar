"""
See https://franklinvp.github.io/2020-06-05-PolyaFooBar/
for the mathematics.
"""

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

def partitionsAndCycleCount(n, factorialTable):
    """
    Iterative algorithm to generate all partitions of 
    the positive integer n.
    In addition to each partition, we compute the following number:
        if the partition has i_1 1s, i_2 2s, ..., i_n ns, we compute
        n!/(1^{i_1}i_1!2^{i_2}i_2!...n^{i_n}i_n!)
    This algorithm comes from https://arxiv.org/abs/0909.2331
    """
    k = 0  # Index of last element in a partition 
    p = n*[0] # To store a partition in p[0:k+1]
    p[0] = n  # First partition is [n]
    result = [] # To store all partitions
    # The loop stops when the current partition has all 1s 
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    result = []
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            partition = a[:k+2]
            result.append((partition, coefficientFactor(partition,n,factorialTable)))
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        partition = a[:k+1]
        result.append((partition, coefficientFactor(partition,n,factorialTable)))
    return result

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

