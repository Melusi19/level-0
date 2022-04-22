def convert(time):
    
    hour = time // 3600
    minutes = time // 60
    time %= 60
    
    if n <= 60:
        return "%02d hour %02d minute " % (minutes, time)
    else:
        return "%02d hours %02d minutes " % (minutes, time)
      
n = 60
print(convert(n))
