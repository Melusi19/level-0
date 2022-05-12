def print_vowels(str): 
    vowels = "aeiouAEIOU"
    result = list()
    for letter in str: 
        l = letter.lower()
        if ( l in vowels ) and (l not in result ):
            result.append(l)
    print (*result, sep=', ')

print_vowels("HEello")
