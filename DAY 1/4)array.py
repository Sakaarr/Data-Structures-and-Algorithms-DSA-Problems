# 🧮 Problem 4: Valid Anagram (Easy)
# 📌 LeetCode #242
# 🔗 Valid Anagram – LeetCode

# ❓ Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An anagram is a word or phrase formed by rearranging the letters of a different word, using all the original letters exactly once.

s = "anagsram"
t = "nagaram"
# if sorted(s) == sorted(t):
#     print(True)
# else:
#     print(False)
    
#Optimized Code using Counter from collections module

from collections import Counter

if Counter(s) == Counter(t):
    print(True)
else:
    print(False)
    
# 🧠 Explanation:
# We use Python’s Counter from the collections module to count the occurrences of each character in both strings.

# Counter(s) creates a dictionary-like object that maps each character to its count.

# Example: "anagram" → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

# "nagaram" → {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

# We then compare the two Counter objects:

# If they’re equal, it means both strings have the exact same characters in the same frequency, so they are anagrams.

# If they’re not equal, then t is not an anagram of s.

# 🚀 Time Complexity:
# O(n), where n is the length of the strings, because we go through the strings once to count the characters.

# This is much more efficient than the brute-force sorting approach.