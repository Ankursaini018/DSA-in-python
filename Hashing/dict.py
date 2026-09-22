users = {}

#inserting values into the dictionary
users["ravi@gmail.com"] = "Ravi"
users["ankur@gmail.com"] = "Ankur"
users["amit@gmail.com"] = "Amit"
users["prachi@gmail.com"] = "Prachi"

print(users)
print(users["amit@gmail.com"])
print("ravi@gmail.com" in users)  # Checking if a key exists in the dictionary


del users["amit@gmail.com"]  # Deleting a key-value pair from the dictionary
print(users)
print(users.keys())
print(users.values())
print(users.items())