def combinationsIterative(n, r):
    """
    Yield, iteratively, all combinations of r elements from the
    elements 0,1,2,...,n-1.
    """
    pool = [x for x in range(n)]
    if r > n:
        return
    indices = [x for x in range(r)]
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def solution(num_buns, num_required):
    """
    Each choice of num_required-1 of the num_buns determines a missing key.
    Therefore, we use binom[num_buns,num_required-1] different keys.
    Each key is used in each num_buns-num_required+1 bunny.
    Therefore, each key is repeated num_buns-num_required+1 times.
    
    To distribute the keys, instead distribute the bunnies to the repeated keys.
    The list of combinations of bunnies that get each repeated key is the same number
    as the keys that we are planning to use. That is 
    
      binom[num_buns,num_required-1] = binom[num_buns,num_buns-num_required+1]
      
    Interpret each combination as the bunnies that will gets the i-th key.
    """
    result = [[] for x in range(num_buns)]
    for key, buns in enumerate(combinationsIterative(num_buns,num_buns-num_required+1)):
        for bun in buns:
            result[bun].append(key)
    return result

