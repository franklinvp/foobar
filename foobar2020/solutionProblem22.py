def solution(s):
    # The current period goes from [0, j)
    # h is reading new characters and r is inside the current period
    #   checking if those characters are equal to those in the period.
    j = 1
    r = 0
    h = 1
    n = len(s)
    if n <= 1:
        return n
    while h < n:
        if s[r] == s[h]:
            r+=1
            h+=1
            if r == j:
                r=0
        else:
            j += max(r,1)
            h = j
            r = 0
    return n//(j)

