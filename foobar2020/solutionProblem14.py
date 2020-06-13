def solution(l):
    if not l:
        return 0
    l.sort(reverse=True)
    rem0 = []
    rem1 = []
    rem2 = []
    total = 0
    for x in l:
        r = x%3
        if r == 0:
            rem0.append(x)
        elif r == 1:
            rem1.append(x)
        else:
            rem2.append(x)
        total += r
    total %= 3
    if total == 0:
        return int("".join([str(x) for x in l]))
    if total == 1:
        if rem1:
            rem1.pop()
        else:
            rem2.pop()
            rem2.pop()
        to_use = rem0+rem1+rem2
        to_use.sort(reverse=True)
        if to_use:
            return int("".join([str(x) for x in to_use]))
        else:
            return 0
    # if total == 2
    if rem2:
        rem2.pop()
    else:
        rem1.pop()
        rem1.pop()
    to_use = rem0+rem1+rem2
    to_use.sort(reverse=True)
    if to_use:
        return int("".join([str(x) for x in to_use]))
    else:
        return 0

