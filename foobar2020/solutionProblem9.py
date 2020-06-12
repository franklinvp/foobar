def baseB(sum,b,k):
    """
    Convert sum to base b with k digits.
    """
    result = []
    while k:
        result.append(sum%b)
        sum //= b
        k-=1
    result.reverse()
    return tuple(result)

def nextID(n,b):
    """
    Compute the next ID.
    The evaluation is a polynomial in b, which
    we do by Horner's method.
    """
    k = len(n)
    d = [int(x) for x in n]
    d.sort()
    D = [d[k-1-i] for i in range(k)]
    M = D[0]
    m = d[k-1]
    sum = D[0]-d[0]
    for i in range(1,k):
        sum *= b
        sum+= int(D[i])-int(d[i])
    return baseB(sum,b,k)

def solution(n,b):
    """
    Detect and compute the length of the cycle
    by the hare and tortoise method. 
    It can also be done by recording all seen IDs 
    in a set(). This is just another method that
    might have to do more computations for the sake 
    of using O(1) memory.
    """
    id1 = tuple([int(x) for x in n])
    id2 = nextID(nextID(id1,b),b)
    while not id1 == id2:
        id1 = nextID(id1,b)
        id2 = nextID(nextID(id2,b),b)
    count = 1
    id2 = nextID(id2,b)
    while not id2 == id1:
        id2 = nextID(id2,b)
        count+=1
    return count

