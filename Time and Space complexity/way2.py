def has_duplicates_fast(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

numbers = [10, 20, 30, 40, 50, 60, 50]

result = has_duplicates_fast(numbers)
if result:
    print("duplicates found (fast)")
else:
    print("no duplicates found (fast)")