def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
nums = [45, 56,67,78,89,90,12,23,34,]
print(linear_search(nums, 123))