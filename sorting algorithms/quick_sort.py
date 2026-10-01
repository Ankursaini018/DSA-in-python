def quick_sort(numbers):
    if len(numbers) <+1:
        return numbers

    pivot = numbers[-1]
    smaller = []
    larger = []

    for number in numbers[:-1]:
        if number <= pivot:
            smaller.append(number)
        else:
            larger.append(number)
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

numbers = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(numbers)) 