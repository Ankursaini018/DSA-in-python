def find_name(names, target):
    left = 0
    right = len(names)-1

    while left<= right:
        middle = (left+right)//2

        if names[middle] == target:
            return middle

        elif names[middle]< target:
            left = middle + 1

        else:
            right = middle - 1

    return - 1
names = ["ankur", "govind", "priyanka", "rishika", "sachin", "sneha"]
target_names = "rishika"

result = find_name(names, target_names)

if result != -1:
    print("found at index", result)
else:
    print("not found")    