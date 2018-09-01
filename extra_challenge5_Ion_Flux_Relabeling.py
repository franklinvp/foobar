def Ion_Flux_Relabeling(h,q):
    """
    Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP
    doomsday device has backfired spectacularly. She had been improving the structure of 
    the ion flux converter tree, but something went terribly wrong and the flux chains 
    exploded. Some of the ion flux converters survived the explosion intact, but others 
    had their position labels blasted off. She's having her henchmen rebuild the ion flux 
    converter tree by hand, but you think you can do it much more quickly - quickly enough, 
    perhaps, to earn a promotion!
    
    Flux chains require perfect binary trees, so Lambda's design arranged the ion flux 
    converters to form one. To label them, she performed a post-order traversal of the 
    tree of converters and labeled each converter with the order of that converter in the 
    traversal, starting at 1. For example, a tree of 7 converters would look like the 
    following:
    
    7 3 6 1 2 4 5
    
    Write a function answer(h, q) - where h is the height of the perfect tree of converters 
    and q is a list of positive integers representing different flux converters - which 
    returns a list of integers p where each element in p is the label of the converter 
    that sits on top of the respective converter in q, or -1 if there is no such converter.
    For example, answer(3, [1, 4, 7]) would return the converters above the converters at 
    indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].
    
    The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary 
    tree containing only the root, h = 2 represents a perfect binary tree with the root 
    and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal
    nodes and four leaf nodes (like the example above), and so forth. The lists q and p 
    contain at least one but no more than 10000 distinct integers, all of which will be 
    between 1 and 2^h-1, inclusive.
    
    Test case 1:
    Inputs: 
    (int) h = 3 
    (int list) q = [7, 3, 5, 1]
    Output: (int list) [-1, 7, 6, 3]

    Test case 2:
    Inputs:
    (int) h = 5 
    (int list) q = [19, 14, 28]
    Output: (int list) [21, 15, 29]
    """
    # Getting all 2^k-1, trains of 1s in binary 
    # for k = 1, 2, 3, ..., h.
    trains = {n+1:(1<<(n+1))-1 for n in range(h)}
    def largest_train(x):
        length = int.bit_length(x)
        thetrain = trains[length]
        # In a lower level language one can
        # simultaneously check if x is a train
        # and get its bit length. Not sure
        # if it is worth it to write such loop
        # in Python.
        if x == thetrain:
            return thetrain
        return trains[length-1]
    def parent(x):
        # The longest train of 1s in 
        # binary is the root.
        if x >= trains[h]:
            return -1
        # Reducing
        # We subtract the largest train
        # smaller than the number until
        # we end up with nothing. 
        diff = int(x)
        lp = largest_train(x)
        while True:
            y = diff
            prev_lp = lp
            lp = largest_train(y)
            diff = y - lp
            if diff == 0:
                break
        # If the last two trains subtracted
        # were equal, then we are on a right
        # child. This means that the parent
        # is one up.
        # Otherwise, we are on a left child.
        # This means that the parent is obtained
        # by adding the last train subtracted,
        # this gives the right sibling, and then
        # adding 1 to get the parent.
        if prev_lp == lp:
            return x + 1
        else:
            return x + lp + 1
    result = [parent(x) for x in q]
    return result
