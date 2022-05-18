def print_vowels(str): 
    vowels = "aeiouAEIOU"
    result = list()
    for letter in str: 
        new_string  = letter.lower()
        if ( new_string  in vowels ) and (new_string  not in result ):
            result.append(new_string )
    print ("Vowels: ", end = '')
    print(*result,sep=', ') 
    
print_vowels("HEello")
