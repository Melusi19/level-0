def celc_to_fahr(celc):
    return (celc * 9 / 5) + 32

def fahr_to_celc(fahr):
    return (fahr - 32) * 5 / 9

print(celc_to_fahr(0))
print(fahr_to_celc(20))
