from math import pow
def is_prime(num):
    print(pow(num, 1/2));
    if num ==2:
        return True
    if num == 0 or num ==1 or num<0 or num%2==0:
        return False
    for i in range(1,num//2, 2):
        print(i)
        if i**2<=num:
            if i ==1:
                continue
            if num%i==0:
                return False
    return True

print(is_prime(522839155390197201))
print(is_prime(1160658307))