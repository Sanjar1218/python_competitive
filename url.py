def domain_name(url):
    x = url.find('//')
    y = url.find('.')
    if x !=-1:
        return (url[x+2:y])
    else:
        lst = url.split('.')
        return (lst[1])


print(domain_name("www.xakep.ru"))
