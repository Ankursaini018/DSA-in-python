def has_duplicates_slow(numbers):
    for i in range (len(numbers)):
        for j in range (len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [10, 20, 30, 40, 50, 60]

result = has_duplicates_slow(numbers)
if result:
    print("duplicates found (slow)")
else:
    print("no duplicates found (slow)")  