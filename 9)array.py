
# 🧩 Problem 13: Intersection of Two Arrays II (Easy)
# 📌 LeetCode #350
# 🔗 Intersection of Two Arrays II – LeetCode

# ❓ Problem Statement:
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Brute Force Approach:
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# output = []
# for num in nums1:
#     if num in nums2:
#         output.append(num)
#         nums2.remove(num)  # Remove the first occurrence of num from nums2
# print(output)  # Output: [2, 2]

# OPTIMIZED CODE
def intersection(nums1, nums2):
    count_map = {}
    result = []
    
    # Step 1: Count frequencies of elements in nums1
    for num in nums1:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    # Step 2: Iterate through nums2 and find common elements
    for num in nums2:
        if num in count_map and count_map[num] > 0:
            result.append(num)
            count_map[num] -= 1  # Decrease count to avoid duplicates
    
    return result

# Test case
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2, 2]

