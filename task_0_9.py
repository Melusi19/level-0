def vowel(word):
    vowels = "AaEeIiOoUu"
    new_char = set(word)
    new_vowels = set (vowels)
    word_list = (new_char & new_vowels)         
    string = ", ".join(word_list).lower()
    return string

print(vowel("HEllo")) 
