def reduce_to_one_dividing_by_one_or_pm_one(n):
    """
    Given n this function computes the minimum number of operations
        1. Divide by 2 when even
        2. Add or subtract 1 when odd
    to reduce n to 1.
    The n input is supposed to be a string containing the decimal 
    representation of the actual number.
    """
    # I don't know if the include test cases in which
    # the conditions given in the challenge are violated.
    # In this one they said that the input was not going to 
    # have more than 309 digits. In an actual submission 
    # you might want to test for the conditions. Or not.
    try:
        n = int(n)
    except:
        return 0
    count = 0
    while not n == 1:
        if n%2 == 0:
            # Divisible by 2, then divide.
            count += 1
            n = n/2
        else:
            if n > 1 and (n-1)%4 == 0:
                # Subtracting 1 will give two 
                # divisions by 2 afterwards.
                count+=1
                n-=1
            else:
                # Adding 1 will create at least
                # two divisions by 2.
                count+=1
                n+=1
    return count
