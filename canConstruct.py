def canCostruct(target, wordBank, memo = {}):
    if target == '':
        return True
    if target in memo.keys():
        return memo[target]
    
    for i in wordBank:
        if target.find(i) == 0:
            s = target[len(i):]
            if canCostruct(s, wordBank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canCostruct('abcdef', ['ab','abc', 'cd', 'def', 'abcd']))
print(canCostruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeee']))