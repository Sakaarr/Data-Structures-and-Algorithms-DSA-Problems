def merge(nums1, m, nums2, n):
    # Pointers for nums1, nums2, and the position to place elements in nums1
    i, j, k = m - 1, n - 1, m + n - 1
    print(i, j, k)  # Debugging statement to check the initial positions

    # Merge the arrays from the end to the beginning
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, place them in nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))  # Output: [1, 2, 2, 3, 5, 6]
