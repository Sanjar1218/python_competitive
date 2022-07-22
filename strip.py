def strip_comments(strng, markers):
    lst = strng.split('\n')
    for i in range(len(strng.split('\n'))):
        for x in range(len(markers)):
            print('this is x',x)
            n = lst[i].find(markers[x])
            if n != -1:  
                print(lst, lst[i])
                lst[i] = lst[i][:n-1 if n>0 else n].rstrip()
    return '\n'.join(lst)


print(strip_comments(['apples, pears # and bananas', 'grapes', 'bananas !#apples'], ["'", '@', '=', '!', ',', '?', '#', '.']))