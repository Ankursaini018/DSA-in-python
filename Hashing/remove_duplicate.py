signups = ["ankur@gmail.com",
           "john@gmail.com",
           "ankur@gmail.com",
           "ankur@gmail.com",
           "ankur@gmail.com",
            "john@gmail.com",
           "rishika@gmail.com",
           "rishika@gmail.com",
           "rishika@gmail.com"]

def remove_duplicates(emails):
    seen = set()
    unique = []

    for email in emails:
        if email not in seen:
            seen.add(email)
            unique.append(email)
    return unique

clean = remove_duplicates(signups)
print(clean)