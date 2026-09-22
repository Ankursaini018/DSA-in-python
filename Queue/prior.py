import heapq

hospital = []

heapq.heappush(hospital, (3, "fracture"))
heapq.heappush(hospital, (1, "heart attack"))
heapq.heappush(hospital, (2, "high fever"))

print(heapq.heappop(hospital))  # Output: (1, "heart attack")
print(heapq.heappop(hospital))  # Output: (2, "high fever")
print(heapq.heappop(hospital))  # Output: (3, "fracture")