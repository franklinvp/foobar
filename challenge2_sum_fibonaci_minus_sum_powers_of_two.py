def sum_fibonaci_minus_sum_powers_of_two(total_lambs):
    """
    I don't remember the original formulation.
    Given total_lambs, an integer between 1 and 1000000000.
    It computes the largest sum of consecutive (modified) Fibonaci numbers 
    which is not greater than total_lambs, the sum of powers of 2
    which is not greater than total_lambs, and subtracts the
    number of terms in each.
    When the sum of powers of 2 cannot be made larger, but adding
    again the last two powers of 2 is still not larger than total_lambs
    then one more term is counted.
    This corresponds to considering lists of non-negative integers that
    sum less than total_lambs, no restrictions on the first two elements,
    but for the remaining elements, each must be not smaller than the sum 
    of the two previous ones, and not smaller than half of the next one.
    Then one is required to find the difference between the lengths of 
    the largest list and the shortest list. Something like that.
    """
    fibo0 = 0
    fibo1 = 1
    fibo2 = 2
    sumFibos = fibo0 + fibo1
    pow2 = 1
    sumPow2 = 1
    countFibs = 0
    countPows = 0
    powerdone = False
    while True:
        fibo2 = fibo1+fibo0
        fibo0 = fibo1
        fibo1 = fibo2
        pow2 *= 2
        if (sumPow2 + pow2 <= total_lambs):
            # Powers of 2 grow faster than Fibonaci
            # So, we are safe counting the Fibos, 
            # while counting the powers of 2.
            countFibs += 1
            countPows += 1
            sumFibos += fibo2
            sumPow2 += pow2
        else:
            if (powerdone == False \
                and sumPow2 + pow2 > total_lambs \
                and total_lambs - sumPow2 >= 3*pow2/4):
                # The powers of 2 already surpassed total_lambs
                # but in this case we can still sneak in an extra 
                # term equal to the sum of the two last terms.
                # It is not going to be possible to include furter terms 
                # after that, otherwise an extra power of  would 
                # have been possible.
                countPows += 1
                powerdone = True
            if (sumFibos + fibo2 > total_lambs):
                # Fibonaci finally surpassed total_lambs
                # time to return what they want.
                return countFibs-countPows
            else:
                # Still possible to add more Fibonaci
                countFibs += 1
                sumFibos += fibo2
