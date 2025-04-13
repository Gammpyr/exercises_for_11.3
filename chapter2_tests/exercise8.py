def is_anagram(string1, string2):
    string1 = string1.replace(' ', '')
    string2 = string2.replace(' ', '')
    return sorted(string1.lower()) == sorted(string2.lower())

