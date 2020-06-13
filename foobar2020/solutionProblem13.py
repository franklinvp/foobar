from functools import cmp_to_key

def compare(a,b):
    A = a.split(".")
    B = b.split(".")
    r = len(A)
    s = len(B)
    n = min(r,s)
    for i in range(n):
        if int(A[i]) < int(B[i]):
            return -1
        elif int(A[i]) > int(B[i]):
            return 1
    if r < s:
        return -1
    elif r > s:
        return 1
    return 0


def solution(l):
    return sorted(l,key=cmp_to_key(compare))

