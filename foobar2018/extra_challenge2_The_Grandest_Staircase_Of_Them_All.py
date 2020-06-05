def The_Grandest_Staircase_Of_Them_All(n):
    """
    Given an integer n compute how many staircasescan be formed 
    with n blocks. The staircases must have at least two steps.
    The steps must have strictly decreasing heights and be of one block width.
    
    Example: With n = 3 there is only the staircase
    
    #
    ##
    
    For n = 4
    
    #
    #
    ##
    
    For n = 5, there are two ways

    #    
    #    #
    #    ##
    ##   ##
    
    n will always be at least 3, but no more than 200.
    """
    # One idea is that the heights of the steps of the staircase
    # is a selection of numbers different numbers 1, 2, 3, ..., n-1
    # such that they add up to n.
    # If A(n,k) is the number of ways to sum n from different numbers from 
    # 1, 2, 3, ..., k, then
    #    A(n, k+1) = A(n - (k + 1), k) + A(n,k)
    # This is because the ways to form n using 1, 2, 3, ..., k+1 consist
    # of the ways to form n using k+1 among the selection, plus the ways to 
    # form it not using k+1. The first is counted by A(n - (k + 1), k), while the
    # second is counted by A(n, k). To compute A(n, n - 1) we just need to 
    # go up the reccurrence relation.
    A = (n + 1)*[0] # To contain A(i, j) in the j-th position, at the i-th iteration.
    A[0] = 1
    for i in range(n - 1):
        for j in range(n, i, -1):
            A[j] += A[j - i - 1]
    return A[n]
