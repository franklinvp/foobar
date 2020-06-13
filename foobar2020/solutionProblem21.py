from collections import defaultdict
def solution(data, n):
    numbers = defaultdict(int)
    for x in data:
        numbers[x]+=1
    result = []
    for x in data:
        if numbers[x] <= n:
            result.append(x)
    return result

