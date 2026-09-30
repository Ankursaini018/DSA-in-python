def binary_search(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        middle = (left +right)//2

        if nums[middle] == target:
            return middle
        elif nums[middle]< target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
nums = [12,23,34,45,56,67,78,89]
print(binary_search(nums, 56))