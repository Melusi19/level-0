def maximum(a,b,c):
    if (a >= b) and (a >= c):
        larger = a

    elif (b >= a) and (b >= c):
        larger = b   

    else:
        larger = c

    return larger

print("The maximum number is", maximum(20, 5, 10))
