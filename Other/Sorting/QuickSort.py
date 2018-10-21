def quick_sort(L):
    _quicksort(L, 0, len(L))

def _quicksort(L, p, q):
    if p < q:
        q = _partition(L, p, r)
        _quicksort(L, p, q - 1)
        _quicksort(L, q + 1, r)

def _partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p,r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    i += 1
    L[i], L[r] = L[r], L[i]
    return i
