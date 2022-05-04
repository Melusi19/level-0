def convert():

    minutes = 350
    hours = 60

    print(minutes//hours, "hours", minutes%hours, "minutes")

convert()

def convert(time):
    
    hour = time // 3600
    minutes = time // 60
    time %= 60
    
    return "%02d hours %02d minutes" % (minutes, time)
      
n = 133
print(convert(n))


def convertor(time):
    
    minutes = 350
    hours = 60
    
    print(minutes//hours, "hours", minutes%hours, "minutes")
    
n = 133
convertor(n)


def convert(time):
    
    minutes = time // 60
    time %= 60
    
    if n <= 60:
        return "%02d hour, %02d minute " % (minutes, time)
    else:
        return "%02d hours, %02d minutes " % (minutes, time)

n = 60      
print(convert(n))