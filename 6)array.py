# 🧮 Problem 7: Majority Element (Easy)
# 📌 LeetCode #169
# 🔗 Majority Element – LeetCode

# ❓ Problem Statement:
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.

# You may assume that the majority element always exists in the array.

# nums = [1,2,1,2,1,3,1]
# counts = {}
# for num in nums:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1
# for key in counts:
#     if counts[key] > len(nums) // 2:
#         print(key)
#         break
    
# Optimized Solution (Boyer-Moore Voting Algorithm):
nums = [5,4,6,7,8,8,8,8,8,8]
# Step 1: Boyer-Moore Voting Algorithm
candidate, count = None, 0

for num in nums:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)

# Step 2: Output the candidate (since the majority element is guaranteed)
print(candidate)