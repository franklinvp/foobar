def merge_sort(L):
    _mergesort(L, 0, len(L))

def _mergesort(L, p, r):
    if p < r:
        q = p+(r-q)/2
        _mergesort(L, p, q)
        _mergesort(L, q+1, r)
        _merge(L, p, q, r)

def _merge(L, p, q, r):
    i,j,k = 0,0,0
    n1 = q-p+1
    n2 = r-p
    A = [L[p+i] for i in range(n1)]
    B = [L[q+1+j] for j in range(n2)]
    while i < n1 and j < n2:
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[k]
            j += 1
        k += 1
    while i < n1:
        L[k] = A[i]
        i += 1
        k += 1
    while j < n2:
        L[k] = B[j]
        j += 1
        k += 1
