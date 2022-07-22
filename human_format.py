def format_duration(seconds):
    #your code here
    second = seconds%60
    minut = seconds//60%60
    hour = seconds//60//60%24
    day = seconds//60//60 //24%365
    year = seconds//60//60 //24//365
    str = ''
    if year>0:
        str+= f"{year}"+ " year" if year ==1 else f"{year}"+ " years"
        if day>0 or hour>0 or minut>0:
            str+=', '
        elif day<0 and hour<0 and minut<0:
            str+=' and '
    if day>0:
        str+= f"{day}" + " day" if day == 1 else f"{day}"+ " days"
        if hour>0:
            str+=', '
    if hour > 0:
        str += f"{hour}"+ " hour" if hour==1 else f"{hour}"+  " hours"
        if minut>0 and second >0:
            str += ", "
        if second==0:
            str+= ' and '
    if minut>0:
        str += f"{minut}"+ " minute" if minut==1 else f"{minut}"+ " minutes"
        if second>0:
            str+=" and "
    if second>0:
        str += f"{second}"+ " second" if second ==1 else f"{second}"+ " seconds"
    return str if len(str)>0 else 'now'

print(format_duration(3660*24*366))