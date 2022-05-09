def maximum(a,b,c):
    if (a >= b) and (a >= c):
        biggest = a

    elif (b >= a) and (b >= c):
        biggest = b   

    else:
        biggest = c

    return biggest

print("The maximum number is", maximum(20,5,10))
