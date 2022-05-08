def find_area(a,b,c):

    s = (a + b + c) * 0.5

    area = (s * (s - a) * (s - b) *(s - c)) ** 0.5

    return area

find_area(2,3,4)