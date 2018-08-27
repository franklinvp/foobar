def number_of_steps_in_slow_gcd(M, F):
    """
    Given strings M and F containing the decimal representation of positive integers 
    m and f, the integers can be transfomed by subtracting the smallest from the largest.
    Output the number of steps needed to reduce the pair to (1,1), if this is 
    possible, as a string containing its decimal representation. 
    Output 'impossible' if this is not possible or if it requires more than 10^50 steps.
    """
    try:
        m = int(M)
        f = int(F)
        count = 0
        while (not m == 1 or not f == 1):
            if (m == 0 or f == 0):
                # One number became 0 and the other is
                # no 1. This is impossible.
                raise
            if m > f:
                if f > 1:
                    # We will be able to subtract f
                    # a m//f times.
                    count += m//f
                    m = m%f
                else:
                    # Done by subtracting 1 a m-1 times
                    count += (m-1)
                    m = 1
            else:
                # Here we can either swap the 
                # numbers and deal with them in 
                # the next loop, or repeat the previous case
                # with the roles of m and f exchanged.
                m, f = f, m # Swapping them.
        result = str(count)
        # The challenge said that if the number of 
        # times was larger than 10^{50} then call it 
        # impossible.
        l = len(result)
        toolong = False
        if l > 50:
            raise
        elif l == 50:
            if not result[0] == '1':
                raise
            for i in range(49):
                if not result[i+1] == '0':
                    raise
        else:
            return result
    except:
        return 'impossible'
