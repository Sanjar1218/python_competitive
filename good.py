def good_vs_evil(good, evil):
    ok = [1,2,3,3,4,10]
    notok = [1,2,2,2,3,5,10]
    n, m= 0,0
    for i in [int(i) for i in good.split(' ')]: 
        ok[n] *= i
        n +=1
    for g in [int(i) for i in evil.split(' ')]: 
        notok[m] *= g
        m+=1
    print(ok)
    print(notok)
    well = sum(ok)
    bad = sum(notok)
    if well < bad:
        return "Battle Result: Evil eradicates all trace of Good"
    elif bad < well:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: No victor on this battle field"

print(good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))