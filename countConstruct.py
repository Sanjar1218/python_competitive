def canCostruct(target, wordBank, memo = {}):
    if target in memo.keys():
        return memo[target]
    if target == '':
        return 1 
    # if target in memo.keys():
    #     return memo[target]
    totalsum = 0 
    for i in wordBank:
        if target.find(i) == 0:
            s = target[len(i):]
            count  = canCostruct(s, wordBank, memo)
            totalsum += count
    memo[target] = totalsum 
    return totalsum 

print(canCostruct('abcdef', ['ab','abc', 'cd', 'def', 'abcd']))
print(canCostruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eee', 'eeeeeeeeeeeeeeeeeeeeeeeeeeeee']))