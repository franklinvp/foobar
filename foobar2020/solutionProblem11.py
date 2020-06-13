def solution(xs):
    """
    Boring case analysis.
    In this problem the pain is just to not miss any case.
    """
    if len(xs)==1:
        return str(xs[0])
    count_neg = 0
    count_pos = 0
    count_zero = 0
    prod_pos = 1
    prod_neg = 1
    max_neg = -float("inf")
    for x in xs:
        if x ==0:
            count_zero+=1
        elif x < 0:
            pos_or_neg = True
            count_neg+=1
            prod_neg *= x
            max_neg = max(max_neg,x)
        elif x > 0:
            count_pos+=1
            pos_or_neg = True
            prod_pos *= x
    if (count_pos == 0 and count_neg == 0) or (count_zero > 0 and count_neg == 1 and count_pos == 0):
        return str(0)
    if count_neg%2!=0:
        count_neg-=1
        prod_neg //=max_neg
    
    if not (count_pos == 0 and count_neg == 0):
        return str(prod_neg*prod_pos)
    return str(0)

