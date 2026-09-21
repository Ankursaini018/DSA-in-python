def clean(names):

    left = 0
    for right in range(len(names)):
        if names[right] != names[left]:
            left = left+1
            names[left] = names[right]
    return left+1

names = ["Alice", "Alice", "Bob", "Ankur", "Charlie", "Rishika", "Charlie"]
count = clean(names)
print(names[:count])