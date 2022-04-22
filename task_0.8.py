def convert(time):
    
    hour = time // 3600
    minutes = time // 60
    time %= 60
    
    return "%02d hours %02d minutes " % (minutes, time)
      
n = 133
print(convert(n))
