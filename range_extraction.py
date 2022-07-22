def solution(args):
    # your code here
    count = 1
    s = ''
    lst = [] 
    b = True
    l = len(args)
    for i in range(l):
        print('args', args[i])
        if i == l-2:
            if args[i] + 1 == args[i+1]:
                count+=1
                if b:
                    lst.append(str(args[i]))
                    b = False
        elif count >= 3:
            lst.append(str(args[i]))
            count=1
            s+= '-'.join(lst) + ','
            lst = []
            b =True
        elif count == 2:
            s+= str(args[i-1])+','+str(args[i])+ ','
            lst = []
            b = True
            count = 1
        else:
            count = 1
            s+=str(args[i]) + ',' 
            lst = []
            b = True
        if i == l-1 and count >= 3:
            lst.append(str(args[i+1]))
            s += '-'.join(lst)
        elif i == l-2:
            # lst.append(str(args[i+1]))
            s += str(args[i])+','
    return s

print(solution([-3,-1,2,10,15,16,17,18,20]))