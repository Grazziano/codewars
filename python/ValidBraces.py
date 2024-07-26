"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""


def valid_braces(string):
    # Define a mapping of closing braces to their corresponding opening braces
    brace_map = {')': '(', '}': '{', ']': '['}
    # Use a stack to keep track of opening braces
    stack = []

    # Iterate over each character in the string
    for char in string:
        if char in brace_map.values():  # If it's an opening brace
            stack.append(char)
        elif char in brace_map.keys():  # If it's a closing brace
            # If the stack is empty or the top of the stack isn't the matching brace
            if not stack or stack.pop() != brace_map[char]:
                return False

    # If the stack is empty, all braces were matched; otherwise, it's invalid
    return len(stack) == 0


print(valid_braces("(){}[]"))    # True
print(valid_braces("([{}])"))    # True
print(valid_braces("(}"))        # False
print(valid_braces("[(])"))      # False
print(valid_braces("[({})](]"))  # False
