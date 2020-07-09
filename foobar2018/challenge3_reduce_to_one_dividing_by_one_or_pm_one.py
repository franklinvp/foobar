def reduce_to_one_dividing_by_one_or_pm_one(n):
    """
    Given n this function computes the minimum number of operations
        1. Divide by 2 when even
        2. Add or subtract 1 when odd
    to reduce n to 1.
    The n input is supposed to be a string containing the decimal 
    representation of the actual number.

    Original problem statement:

    Fuel Injection Perfection
    =========================

    Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for 
    her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe 
    sneak in a bit of sabotage while you're at it - so you took the job gladly. 

    Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the 
    LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel 
    intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet 
    at a time. 

    The fuel control mechanisms have three operations: 

    1) Add one fuel pellet
    2) Remove one fuel pellet
    3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum 
       antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even 
       number of pellets)

    Write a function called solution(n) which takes a positive integer as a string and returns the minimum number 
    of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a 
    number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

    For example:
    solution(4) returns 2: 4 -> 2 -> 1
    solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit Solution.java

    Test cases
    ==========
    Your code should pass the following test cases.
    Note that it may also be run against hidden test cases not shown here.

    -- Python cases --
    Input:
    solution.solution('15')
    Output:
        5

    Input:
    solution.solution('4')
    Output:
        2

    -- Java cases --
    Input:
    Solution.solution('4')
    Output:
        2

    Input:
    Solution.solution('15')
    Output:
        5
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
