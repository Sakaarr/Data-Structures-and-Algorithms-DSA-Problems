# 🧩 Problem 19: Count of Elements with Strictly Smaller Elements
# (A variation of frequency counting / sorting problems)

# ❓ Problem Statement:
# Given an array of integers nums, return a new array result where result[i] is the count of elements in nums that are strictly smaller than nums[i].

# ✅ Example:
# python
# Copy
# Edit
# Input: nums = [8, 1, 2, 2, 3]
# Output: [4, 0, 1, 1, 3]
# For 8, there are 4 smaller elements: [1, 2, 2, 3]

# For 1, there are 0 smaller elements.

# For both 2s, there’s only 1 smaller element: [1]

# For 3, there are 3 smaller elements: [1, 2, 2]

#BRUTE FORCE SOLUTION:
def smallerNumbersThanCurrent(nums):
    result = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)

    return result

# Example:
print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # Output: [4, 0, 1, 1, 3]


#OPTIMIZED SOLUTION:

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    num_to_count = {}

    # Map number to its first occurrence index in the sorted list
    for i in range(len(sorted_nums)):
        if sorted_nums[i] not in num_to_count:
            num_to_count[sorted_nums[i]] = i

    # Build the result using the mapping
    result = [num_to_count[num] for num in nums]
    return result

# Example:
print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # Output: [4, 0, 1, 1, 3]

    
