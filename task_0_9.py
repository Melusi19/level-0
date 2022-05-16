def print_vowels(str): 
    vowels = "aeiouAEIOU"
    result = list()
    for letter in str: 
        l = letter.lower()
        if ( l in vowels ) and (l not in result ):
            result.append(l)
    print ("Vowels: ", end = '')
    #Sep is a parameter in python that primarily formats the printed statements
    print(*result,sep=', ') 
    
print_vowels("HEello")
