from collections import defaultdict

# Possible preimages of a point
# The results are encoded as pairs of numbers (a,b)
# where a,b are between 0 and 3, inclusive.
# Their digits, in binary represent the rows of 
# a preimage.
preimages = {
    0: [[0,0],
        [0,3],
        [1,1],
        [1,2],
        [1,3],
        [2,1],
        [2,2],
        [2,3],
        [3,0],
        [3,1],
        [3,2],
        [3,3],],
    1: [[0,1],
        [1,0],
        [0,2],
        [2,0],
        ]
    }

def columnToNumber(col):
    """
    Interpret a column as the binary representation of a number.
    """
    number = 0
    for elem in col:
        number <<= 1
        number += elem
    return number

def preimageColumnToNumber(preimcol):
    """
    The preimage of a colum is input as a list of pairs of numbers

        [[a,b],[b,c],[c,d],...,[y,z]]

    The numbers a,b,c,..., which are between 0 and 3, inclusive,
    represent a row of an nx2 preimage of a column.
    This computes two numbers which represent the two columns of 
    this preimage.
    """
    leftnumber = 0
    rightnumber = 0
    for elem in preimcol:
        leftnumber <<= 1
        rightnumber <<= 1
        leftnumber += (elem&2) >> 1
        rightnumber += elem&1
    return (leftnumber,rightnumber)
    

def preimagesOfColumnsMap(columns):
    """
    Build map sending 
    
        (column, 
         first column of possible preimage) -> second column of possible preimage
         
    We do this by doing DFS along the directed graph of preimages of each point.
    Two preimages of points are considered connected when the bottom
    of one coincides with the top of the other.
    """
    mapping = defaultdict(set)
    for col in columns:
        # Do DFS to produce the preimages
        totalpreim_thiscol = []
        for preim in preimages[col[0]]:
            columnPreimages = []
            depth = 0
            # In each element of the stack the first entry is the 
            # current depth. The remaining elements are the nodes in the path.
            stack = [[depth,preim]]
            while stack:
                depth, currentPath = stack.pop()
                if depth == len(col)-1:
                    columnPreimages.append(currentPath)
                else:
                    for nextpreim in preimages[col[depth+1]]:
                        if nextpreim[0] == currentPath[-1]:
                            stack.append([depth+1,currentPath + [nextpreim[1]]])
            totalpreim_thiscol += columnPreimages
        for x in totalpreim_thiscol:
            preim = preimageColumnToNumber(x)
            mapping[(columnToNumber(col),preim[0])].add(preim[1])
    return mapping

def solution(g):
    # Transpose, to work first along the potentially smaller dimension
    g = tuple(zip(*g)) 
    # Unique columns to compute their possible preimages
    columns = tuple(set(g))
    mapping = preimagesOfColumnsMap(columns)
    colAsNumbers = [columnToNumber(x) for x in g]
    # Dynamic Programming counting of the number of possible preimages.
    # At each step, for each possible ending column of a preimage, we keep the count of how many
    # preimage-matchings of the columns analyzed so far end in this column ending.
    count = 0
    # Each column ending sent to the number of preimages for the group of columns analyzed so far.
    # At the beginning an empty number of  columns have been analyzed so far. 
    # For each ending we have the empty preimage having that ending.
    preimageCount = {i: 1 for i in range(1<<(len(g[0])+1))}
    for row in colAsNumbers:
        nextColumn = defaultdict(int)
        for c1 in preimageCount:
            for c2 in mapping[(row, c1)]:
                nextColumn[c2] += preimageCount[c1]
        preimageCount = nextColumn
    ret = sum(preimageCount.values())
    return ret
    return count


Input1 = [
    [True, False, True], 
    [False, True, False], 
    [True, False, True],
    ]

Input2 = [
    [True, False, True, False, False, True, True, True], 
    [True, False, True, False, False, False, True, False], 
    [True, True, True, False, False, False, True, False], 
    [True, False, True, False, False, False, True, False], 
    [True, False, True, False, False, True, True, True],
    ]

Input3 = [
    [True, True, False, True, False, True, False, True, True, False], 
    [True, True, False, False, False, False, True, True, True, False], 
    [True, True, False, False, False, False, False, False, False, True], 
    [False, True, False, False, False, False, True, True, False, False],
    ]

AResult4 = [
    [False, True, False, False, True, True, True, False, True, True, True, True, False, True, True, False, False, False, False, False, False, False, True, False, True, True, True, True, True, False, False, True, True, True, False, True, False, False, True, False, True, True, True, False, True, False, True, False, True, True,True], 
    [False, True, True, False, True, True, False, True, True, True, True, True, False, False, True, True, False, True, False, False, False, True, True, True, False, True, True, True, False, True, False, False, False, True, True, True, False, True, True, False, False, False, False, True, False, False, False, True, True, True,True], 
    [True, False, False, True, False, False, False, False, True, True, True, False, True, False, False, False, False, True, False, True, False, True, True, False, False, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True, False, False, False, True, False, False, False, False, False, True,True], 
    [False, False, False, False, True, False, True, False, True, False, True, False, False, True, True, True, False, True, False, True, False, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True, False, True, False, False, False, True, True, True, False, False, False, False, True, True,True], 
    [True, True, True, True, False, False, False, False, True, False, False, False, True, False, True, True, True, True, True, False, False, True, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, False, True, True,True, True, True, False, True, True,True], 
    [False, True, True, True, False, True, False, True, True, True, False, False, True, True, False, False, False, False, True, True, True, True, True, False, True, False, True, True, False, True, True, False, True, False, False, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True,True], 
    [True, True, True, True, True, False, True, True, True, False, False, True, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True, False, False, False, True, False, True, True, False, False, True, True, False, False, False, True, False, False, False, True, True, True,True, True,True], 
    [True, True, True, False, False, False, True, True, False, False, False, True, False, False, False, False, True, False, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, True, True, True, True,True, False], 
    [True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, True, True, True, True, False, False, True, True, True, True, True, True, True, False, False, False, True, False, False, True, True, True, True, True,True],
    [False, True, True, True, False, True, False, True, True, True, False, False, True, True, False, False, False, False, True, True, True, True, True, False, True, False, True, True, False, True, True, False, True, False, False, True, True, True, True, False, False, False, False, False, True, True, True, True, True, True,True], 
    ]

Input4 = [
    [False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False, False, True, True, False, False, False, False], 
    [False, False, False, False, False, True, True, False, False, False, False, False, True, True, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False], 
    [True, False, True, False, True, True, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, True, False, False], 
    [False, False, False, False, True, True, True, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False], 
    [False, False, False, False, True, True, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, True, True, False, False, False, False, True, True, False, False, False, True, False, True, True, False, True, False, False, False, False, False, False], 
    [False, False, False, False, True, False, False, False, True, False, False, False, True, True, True, False, False, False, False, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False], 
    [False, False, False, False, False, False, False, True, False, False, True, True, False, False, True, False, True, True, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False], 
    [False, False, False, False, False, False, True, False, False, True, False, True, False, True, True, True, False, True, False, False, False, False, True, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False]
    ]

AResult = [
    [False,True,False,False],
    [False,False,True,False],
    [False,False,False,True],
    [True,False,False,False],
    ]


print(solution(Input1))
print(solution(Input2))
print(solution(Input3))
#print(answer(Input4))

