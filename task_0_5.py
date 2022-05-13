def area_of_a_triangle(a,b,c):

    semiperimeter = (a + b + c) * 0.5

    area = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) *(semiperimeter - c)) ** 0.5

    return area

print(area_of_a_triangle(3,4,5))
