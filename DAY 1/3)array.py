# 🧮 Problem 3: Contains Duplicate (Easy)
# 📌 LeetCode #217
# 🔗 Contains Duplicate – LeetCode

# ❓ Problem Statement:
# Given an integer array nums, return true if any value appears at least twice in the array, and false if every element is distinct.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1]

# for num in nums:
#     if nums.count(num) > 1:
#         print(True)
#         break
# else:
#     print(False)
    
#Optimized Code using SET
seen = set()
for num in nums:
    if num in seen:
        print(True)
        break
    seen.add(num)
else:
    print(False)
