def convert(time):
    hour = time // 60
    minutes = (time % 60)

    if hour <= 1:
        print(f" {str(hour)} hour , {str(minutes)} minute ")
    else:
        print(f" {str(hour)} hours , {str(minutes)} minutes ")    

convert(61) 