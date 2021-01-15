import random

def merge(l1, l2):
    l3 = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            l3.append(l1.pop(0))
        else:
            l3.append(l2.pop(0))
    l3 += l1 + l2

    return l3

def merge_sort(nums):
    if len(nums) < 2:
        return nums

    half = len(nums) // 2
    first_half = nums[:half]
    second_half = nums[half:]

    n1 = merge_sort(first_half)
    n2 = merge_sort(second_half)

    return merge(n1, n2)

nums = list(range(20))
random.shuffle(nums)
print('Original:\n', nums)
nums = merge_sort(nums.copy())
print('Sorted:\n', nums)