"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def word_score(word):
    # Compute the score of a single word
    return sum(ord(char) - ord('a') + 1 for char in word)


def high_score_word(s):
    words = s.split()
    highest_score = 0
    highest_word = ""

    for word in words:
        score = word_score(word)
        if score > highest_score:
            highest_score = score
            highest_word = word
        # No need to handle the case where scores are equal since the first word encountered with that score will be retained

    return highest_word


# Examples
print(high_score_word("abad czar"))     # Output: "czar"
print(high_score_word("hello world"))   # Output: "world"
print(high_score_word("a ab abc"))      # Output: "abc"
