def vowel(word):

    vowels = "aeiou"
    vow = [letter for letter in word.lower() if letter in vowels]
    print(",".join(vow))

vowel("HEllo")
