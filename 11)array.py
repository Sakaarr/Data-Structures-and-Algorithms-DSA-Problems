# 🧩 Problem 16: Remove Duplicates from Sorted Array (Easy)
# 📌 LeetCode #26
# 🔗 Remove Duplicates from Sorted Array – LeetCode

# ❓ Problem Statement:
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def remove_duplicates(nums):
    # Edge case: if the list is empty, return 0
    if not nums:
        return 0
    
    # Initialize unique_pos as the position where the next unique element should go
    unique_pos = 1
    
    # Iterate through the list starting from index 1 (since index 0 is always unique)
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            # If the current number is different from the previous one, place it at unique_pos
            nums[unique_pos] = nums[i]
            unique_pos += 1  # Increment unique_pos
    
    # The length of the unique array is unique_pos
    return unique_pos, nums[:unique_pos]

# Test case
print(remove_duplicates([0, 0, 1, 1, 2, 2, 3, 3, 4]))  # Output: (5, [0, 1, 2, 3, 4])
