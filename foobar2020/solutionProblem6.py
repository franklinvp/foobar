def solution(l):
    """
    My first thought to compute the sum of the elements of the square of 
    the adjacency matrix of the graph. That takes too long.
    Since we only need totals, we compute how many edges end at a vertex
    and how many start at a vertex. The dot product of these vectors
    gives the number of paths of length 2.
    The dot product can be distributed with respect to the addition of the 
    vector storing the number of edges ending at a vertex. So, it can be
    accumulated along the way.
    """
    n = len(l)
    if n <= 2:
        return 0
    number_of_pairs_ending_in = n*[0]
    number_lucky_pairs = 0
    for i in range(n):
        for j in range(i):
            if l[i]%l[j]==0:
                number_of_pairs_ending_in[i] += 1
                number_lucky_pairs += number_of_pairs_ending_in[j]
    return number_lucky_pairs

