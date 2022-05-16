def common_letters(str1, str2):
    common = ""
    for letter in str1.lower():
        if letter in str2.lower():
            common += letter 
    return "Common letters: " + ', '.join(common)

print(common_letters("house","computers"))
