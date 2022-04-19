def maximum(a,b,c):

    if(a >= b) and (a <= c):
        larger = a 

    elif(b >= a) and (b >= c):
        larger = b

    else:
        larger = c

    return larger

a = 6
b = 12
c = 1
print(maximum(a,b,c))
