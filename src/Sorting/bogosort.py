import random

def bogosort(nums):
    nums = nums.copy()
    while nums != list(range(len(nums))):
        random.shuffle(nums)

    return nums

nums = list(range(5))
random.shuffle(nums)
print("Before:\n", nums)
nums = bogosort(nums)
print('After:\n', nums)