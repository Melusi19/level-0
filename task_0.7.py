def convert_cels_to_fah(n):

    return(n * 1.8) + 32

n = 20
print(int(convert_cels_to_fah(n)))

def convert_fah_to_cels(m):
    
    return (m-32)*0.55
    
m = 20
print(int(convert_fah_to_cels(m)))