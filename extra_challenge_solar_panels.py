def solar_panels(area):
    """
    Given area, this function outputs a list containing the 
    largest perfect squares that can be extracted from what remains 
    from area.
    Example:
        If area = 12, then 9 is the largest square, and 3 remains
        from where 1 is the largest perfect square, and 2 remains,
        from where 1 is again the largest square, and 1 remains,
        from which finally 1 is again the largest square.
        Therefore, the out put would be the list 
            [9,1,1,1]
    """
    # For this one one only needs to compute square root, subtract 
    # and repeat. I don't think the challenge's testcases had very large inputs
    # but if they did, or if one wants it to work for very large inputs,
    # then one should avoid the temptation of using floating point 
    # square roots. Instead compute integer square root
    #    (https://en.wikipedia.org/wiki/Integer_square_root)
    def isqrt_Newton(n):
        """
        Integer square root using Newton's method
        """
        x0 = n
        x1 = (n+1)//2
        while not x1 == x0 and not x1 == x0+1:
            x1, x0 = (x1 + n//x1)//2, x1
        return x0
    def isqrt_bitwise(n):
        """
        Computes the integer square root 
        of n using bitwise operations.
        """
        if n < 0:
            raise
        shift = 2
        nShifted = n >> shift
        while not nShifted == 0 and not nShifted == n:
            shift += 2
            nShifted = n >> shift
        shift -= 2
        result = 0
        while shift >= 0:
            result = result << 1
            candidateResult = result + 1
            if candidateResult * candidateResult <= (n >> shift):
                result = candidateResult
            shift -= 2
        return result
    # The actual computation        
    result = []
    while area > 0:
        # Compute the square of the integer square root.
        square = int(isqrt_bitwise(area))**2
        # Add to the list the square as many times as it divides the
        # total area, and repeat
        result += (area // square) * [square]
        area %=square
    return result
