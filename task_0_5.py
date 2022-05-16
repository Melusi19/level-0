def area_of_a_triangle(num1,num2,num3):

    semiperimeter = (num1 + num2 + num3) * 0.5

    area = (semiperimeter * (semiperimeter - num1) * (semiperimeter - num2) *(semiperimeter - num3)) ** 0.5

    return area

print(area_of_a_triangle(3,4,5))
