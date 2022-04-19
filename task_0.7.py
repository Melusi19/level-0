def ConvertCtoF(n):

    return(n * 1.8) + 32

n = 15
print(int(ConvertCtoF("Temperature in Fahrenheit is: " + n)))

def ConvertFtoC(m):

    return((m -32)*5) / 9

m = 40
print(int(ConvertFtoC("Temperature in Celsius is: " + m)))