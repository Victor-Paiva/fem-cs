import random

def quickSort(nums):
    if len(nums) < 2:
        return nums

    pivot = nums[-1]
    left, right = [], []
    for i in range(len(nums) - 1):
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])

    return quickSort(left) + [pivot] + quickSort(right)

nums = list(range(20))
random.shuffle(nums)
print('Before:\n', nums)
nums = quickSort(nums)
print('After:\n', nums)