# 🧩 Problem 12: Intersection of Two Arrays (Easy)
# 📌 LeetCode #349
# 🔗 Intersection of Two Arrays – LeetCode

# ❓ Problem Statement:
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

def intersection(nums1, nums2):
    # Step 1: Convert both lists to sets to remove duplicates
    set1 = set(nums1)
    set2 = set(nums2)

    # Step 2: Find the intersection of both sets
    result = set1.intersection(set2)

    # Step 3: Convert the result back to a list and return it
    return list(result)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]