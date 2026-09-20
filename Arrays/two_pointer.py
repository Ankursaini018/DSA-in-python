def find_two_numbers(numbers, target):
    left = 0
    right = len(numbers)-1

    while left<right:
        total = numbers[left] + numbers[right]

        if total == target:
            return[numbers[left], numbers[right]]

        elif total> target:
            right = right-1

        else:
            left = left-1

    return[]

numbers = [1, 3, 5, 6, 8, 11]
print(find_two_numbers(numbers,9))
print(find_two_numbers(numbers,14))