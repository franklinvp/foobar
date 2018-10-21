"""
Binary heap:
    - Array representing a binary tree
    - The binary tree's levels are all complete, except
      possibly for the list one, which is filled from the left.
    - Carries two properties:
          - Length of the array
          - heap_size, which is <= length
          
Max heap:
    - Binary heap A
    - For every node i (except the root)
          A[parent(i)] >= A[i]
"""

def parent(x):
    return x//2

def left(x):
    return 2*i

def right(x):
    return 2*i+1

# Here A is only a list and the properties of the heap are passed as parameters.
# One could encapsulate the behavior in a class
def max_heapify(A, heap_size, i):
    l = left(i)
    r = right(i)
    if l <= heap_size and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r-1] > A[largest - 1]:
        largest = r
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        max_heapify(A, heap_size, largest)

def build_max_heap(A):
    heap_size = len(A)
    for i in range(heap_size//2, 0, -1):
        max_heapify(A, heap_size, i)
    return heap_size

def heap_sort(A):
    heap_size = build_max_heap(A)
    for i in range(len(A), 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        heap_size -= 1
        max_heapify(A, heap_size, 1)
