# 🧩 Problem 14: Move Zeroes (Easy)
# 📌 LeetCode #283
# 🔗 Move Zeroes – LeetCode

# ❓ Problem Statement:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

input_array = [0, 1, 0, 3, 12]

last_non_zero = 0
# Step 1: Move all non-zero elements to the front
for i in range(len(input_array)):
    if input_array[i] != 0:
        input_array[last_non_zero], input_array[i] = input_array[i], input_array[last_non_zero]
        last_non_zero += 1
# Step 2: Fill the remaining positions with zeros
for i in range(last_non_zero, len(input_array)):
    input_array[i] = 0
print(input_array)  # Output: [1, 3, 12, 0, 0]