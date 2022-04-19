def findArea(a,b,c):

    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("The area of the triangle is: " + area)

    a = 2
    b = 5
    c = 1

    findArea(a,b,c)