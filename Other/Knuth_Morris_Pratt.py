"""
Searching all the occurrences of a pattern of characters inside another.

    P = word or patter to be searched
    T = word in which the pattern is going to be searched

For a word P, define P_k to be the word formed by its k first letters.

Prefix function:

    prefix: {1,2,...,m} --> {0,1,...,m-1}
    prefix(q) = max{k: k < q and P_k is a sufix of P_q}

This is, the function gives the longest prefix of P that is a proper sufix of P_q.
This tells us how much to jump after a failed match. Failing a match means that 
we have found a prefix of P. A sufix of such prefix is a potential starting point
for a new search if that sufix is a prefix of P.

The other cool thing is that 

    prefix^*(q) = {prefix(q), prefix^2(q), ...}
                = {k: k < q and P_k is a sufix of P_q}

This allows for an efficient computation of the prefix function.

Example:
    P = 'aac'
    T = 'aaacaacaac'
    prefix = [-1, 0, 1, 0]
    matching_positions = [1, 4, 7]
"""

def kmp_prefix_function(P):
    m = len(P)
    prefix = (m+1)*[-1]
    for i in range(m):
        prefix[i+1] = prefix[i] + 1
        while prefix[i+1] > 0 and P[i] != P[prefix[i+1]-1]:
            prefix[i+1] = prefix[prefix[i+1]-1]+1
    return prefix

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    prefix = kmp_prefix(P)
    result = []
    j, k = 0, 0
    while j < n:
        if P[k] == T[j]:
            j += 1
            k += 1
            if k == n:
                result.append(j-k)
                k = prefix[k]
        else:
            k = prefix[k]
            if k < 0:
                j += 1
                k += 1
    return result
