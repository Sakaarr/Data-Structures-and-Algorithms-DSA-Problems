# 🧩 Problem 20: Valid Parentheses
# 📌 LeetCode #20
# 🔗 Valid Parentheses – LeetCode

# ❓ Problem Statement:
# Given a string s containing just the characters:

# '(', ')'

# '{', '}'

# '[', ']'

# Determine if the input string is valid.

# ✅ Rules for Validity:
# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.

# Every closing bracket must have a corresponding opening bracket.


def isValid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False

    return stack == []


print(isValid("()"))  # Output: True
print(isValid("{[]}"))  # Output: True
print(isValid("([)]"))  # Output: False