def find_area(a,b,c):
    
    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The area of the triangle is %f' %area)

a = 3.0
b = 4.0
c = 5.0
    
find_area(a,b,c)