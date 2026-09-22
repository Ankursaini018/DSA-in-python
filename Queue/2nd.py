from collections import deque
queue = deque()

queue.append("Rishika")
queue.append("Ankur")
queue.append("Amit")
queue.append("prachi")
print(queue)

first = queue.popleft()
print(first)
print(queue)

print(queue[0])  # Accessing the first element without removing it
print(len(queue))  # Getting the size of the queue
print(len(queue) == 0)  # Checking if the queue is empty