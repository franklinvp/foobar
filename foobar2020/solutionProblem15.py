def solution(x, y):
    """
    The number in the downhill diagonal through the point (x,y)
    is the triagular number for the input x+y-1. To get the value we subtract 
    from this triagular number the value of y-1.
    Recall that the n-th triangular number is n(n+1)/2.
    """
    summa = x+y
    return str((((summa-1)*summa)>>1)-(y-1))

