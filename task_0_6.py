def maximum(*args):
    maxi_num = args[0]
    for i in args:
        if i > maxi_num:
            maxi_num = i
    return maxi_num

print(maximum(20,5,10,7,25))
