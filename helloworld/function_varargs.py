def func(init,*numbers,**keywords):
    count = init
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print func(2,3,4,5,value1=6,value2=7)
