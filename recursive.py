def replicate(times, number):
    #your code here
    if times<=0:
        return []

    lst = replicate(times-1, number)
    lst.append(number)
    return lst

print(replicate(8, 5))