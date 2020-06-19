def solution(pegs):
    """
    Sequence a_n is defined by

        a_0=0 and
        a_{i+1}=a_i+(-1)^i(pegs_{i+1}-pegs_i)

    Withs these, the radii of the wheels are

        r_i = (-1)^{i-1}(a_i-r)

    where r is the radius of the first wheel.
    We impose that r=2*r_{n-1} and that r_i>=1.
    The latter condition is not very clear in the problem.
    In the statement it can seem like they only ask this condition
    for the radius of the first wheel.
    """
    n = len(pegs)
    if n<2:
        return (-1,-1)
    an = 0
    pm_one = -1
    max_even_a = -float("inf")
    min_odd_a = float("inf")
    for i in range(n-1):
        an -= pm_one*(pegs[i+1]-pegs[i])
        pm_one *=-1
        if not i&1:
            min_odd_a = min(min_odd_a, an)
        else:
            max_even_a = max(max_even_a, an)
    numerator = 2*an
    denominator = abs(1+2*pm_one)
    if numerator < denominator*(max_even_a+1) \
        or numerator > denominator*(min_odd_a-1):
        return (-1,-1)
    if pm_one == 1 and numerator%3==0:
        numerator //=3
        numerator = abs(numerator)
        denominator = 1
    return (numerator, denominator)

