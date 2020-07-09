def reduce_to_one_dividing_by_one_or_pm_one(n):
    """
    Given n this function computes the minimum number of operations
        1. Divide by 2 when even
        2. Add or subtract 1 when odd
    to reduce n to 1.
    The n input is supposed to be a string containing the decimal 
    representation of the actual number.
    """
    count = 0
    while not n == 1:
        if not n & 1:
            # Divisible by 2, then divide.
            count += 1
            n //= 2
        else:
            n_minus_1 = n-1
            if (n == 3) or (n > 1 and n_minus_1 % 4 == 0):
                # Subtracting 1 will give two 
                # divisions by 2 afterwards.
                # The case n = 3 gives only one zero but
                # that one division by 2 finishes it.
                count += 1
                n = n_minus_1
            else:
                # Adding 1 will create at least
                # two divisions by 2.
                count += 1
                n += 1
    return count
