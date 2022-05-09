def common_characters(str1, str2):
    ch1 = set(str1)
    ch2 = set(str2)

    intersection = ch1.intersection(ch2)
    common = ", ".join(intersection)

    print(f"Common letters: {common}")