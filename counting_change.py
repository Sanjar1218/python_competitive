def count_change(money, coins):
    n = 0
    if money==0:
        return n+1
    if money<0:
        return None 
    for  i in coins:
        remainder = money-i
        x = count_change(remainder, coins)
        print('count', x)
        if x == 1:
            return n
    return 1 
    # your implementation here
print(count_change(4, [1,2]))