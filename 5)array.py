# 🧮 Problem 5: Move Zeroes (Easy)
# 📌 LeetCode #283
# 🔗 Move Zeroes – LeetCode
# ❓ Problem Statement:
# Given an array nums, write a function that moves all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in place without making a copy of the array.

# nums = [0, 1, 0, 3, 12]

# # Step 1: Create a new list of all non-zero elements
# non_zero = [num for num in nums if num != 0]

# # Step 2: Add zeros to the end to match original list size
# non_zero += [0] * (len(nums) - len(non_zero))

# # Step 3: Copy the result back to the original list
# for i in range(len(nums)):
#     nums[i] = non_zero[i]

# print(nums)


#OPTIMZED CODE
nums = [0, 1, 0, 3, 12]
last_non_zero = 0

# Step 1: Move all non-zero elements to the front
for i in range(len(nums)):
    if nums[i] != 0:
        nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
        last_non_zero += 1

print(nums)