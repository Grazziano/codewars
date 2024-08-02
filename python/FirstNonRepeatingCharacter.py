"""
Write a function named first_non_repeating_letter† that takes a string input, and returns
the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter
t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but
the function should return the correct case for the initial letter. For example, the input
'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function
should handle any Unicode character.
"""


def first_non_repeating_letter(s):
    lower_s = s.lower()
    char_count = {}

    # Contar a ocorrência de cada caractere na string em minúsculas
    for char in lower_s:
        char_count[char] = char_count.get(char, 0) + 1

    # Encontrar o primeiro caractere não repetido na string original
    for i in range(len(s)):
        if char_count[lower_s[i]] == 1:
            return s[i]

    return ""


print(first_non_repeating_letter('stress'))  # Output: 't'
print(first_non_repeating_letter('sTreSS'))  # Output: 'T'
print(first_non_repeating_letter('aA'))      # Output: ''
print(first_non_repeating_letter('moonmen'))  # Output: 'e'
print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))  # ,
