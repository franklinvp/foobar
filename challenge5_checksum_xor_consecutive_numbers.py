def checksum_xor_consecutive_numbers(start, length):
    """
    The numbers start, start+1, start+2,...
    are placed in a square of side length.
    Consider the top-left half of the matrix,
    including the anti-diagonal.
    This function returns the xor of all those numbers.
    The challenge said that the total number of entries 
    of the matrix was not going to be larger than 2000000000.
    Or maybe that the sum of the element was not going to be 
    larger than that. Something like that to tell you 
    that there could be a large number of elements to xor,
    but also not insanely many. Reducing from quadratic 
    to linear turned out to be enough.
    """
    def xorconsec(a,b):
        """
        This function return the xor of all integers
        between a, and b, including both.
        """
        # The xor-ory gets reduced by taking into account 
        # that an even number xor-ed with its successor 
        # results in 1, and that 1 xor 1 = 0.
        if a > b:
            return 0
        L = b-a+1
        R = L%4
        aeven = a%2
        if R == 0:
            if aeven == 0:
                return 0
            else:
                return a^b^1
        elif R == 1:
            if aeven == 0:
                return b
            else:
                return a
        elif R == 2:
            if aeven == 0:
                return (b-1)^b
            else:
                return a^b
        elif R == 3:
            if aeven == 0:
                return b^1
            else:
                return a^1
    checksum = 0
    for size in range(length, 0, -1):
        a = start
        b = start + size - 1
        result = xorconsec(a,b)
        checksum ^= result
        start += length
    return checksum
