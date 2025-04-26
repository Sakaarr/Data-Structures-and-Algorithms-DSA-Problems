# 🧮 Problem 8: Two Sum II - Input Array Is Sorted (Easy)
# 📌 LeetCode #167
# 🔗 Two Sum II – LeetCode

# ❓ Problem Statement:
# You are given a 1-indexed, sorted array of integers numbers (in non-decreasing order), and a target integer target.

# Return the indices of the two numbers such that they add up to target.

# The answer must be returned as a list [index1, index2] of the two numbers’ indices, where index1 < index2.

# Each input has exactly one solution, and you may not use the same element twice.
# FOR UNSORTED ARRAY
# nums = [0,2, 7, 11, 15]
# target = 15
# num_map = {}  # value -> index
# for i, num in enumerate(nums):
#     complement = target - num
#     if complement in num_map:
#         print([num_map[complement], i])
#         break
#     num_map[num] = i
    
    
# FOR SORTED ARRAY
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]

        if curr_sum == target:
            return [left + 1, right + 1]  # 1-indexed output
        elif curr_sum < target:
            left += 1  # Need a bigger sum
        else:
            right -= 1  # Need a smaller sum
numbers = [2, 7, 11, 15]
target = 13
print(twoSum(numbers, target)) 