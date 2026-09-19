marks = [85, 90, 78, 92, 88]


########accessing elements in the list O(1)
# print(marks[0])
# print(marks[2])
# print(marks[-2])


### inserting elements in the end of list O(1)
# marks.append(100)
# print(marks)

# ### inserting elements in the middle of list O(n)
# marks.insert(2,95)
# print(marks)


###deleting elements from the end of list O(1)
# marks.pop(1)
# print(marks)
# marks.remove(78)
# print(marks)


### slicing in list O(k) where k is the size of the slice
print(marks[1:4])
print(marks[::-1]) 
print(marks[::2])
