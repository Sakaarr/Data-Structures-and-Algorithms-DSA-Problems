# ❓ Problem Statement:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 📌 Problem Link: Two Sum – LeetCode #1
# input = [4, 4, 5, 3]
# target = 8

# output = []

# for i in range(len(input)):
#     for j in range(i+1, len(input)):
#         if input[i]+input[j] == target:
#             if input[i]!= input[j]:
#                 output.append(input[i])
#                 output.append(input[j])
#                 break   
        
# print(output)

#Optimized Code using HASHMAP
nums = [3, 2, 1, 0,9,10,4,5,6,7,8]
target = 8
num_map = {}  # value -> index

for i, num in enumerate(nums):
    complement = target - num
    # print(complement)
    print(num_map)
    if complement in num_map:
        print([num_map[complement], i])
        break
    num_map[num] = i
