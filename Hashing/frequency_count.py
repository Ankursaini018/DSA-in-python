todays_orders = ["apple", "banana", "apple", "orange", "banana", "apple"]

def count_orders(orders):
    freq = {}
    for dish in orders:
        if dish in freq:
            freq[dish] = freq[dish] + 1
        else:
            freq[dish] = 1
    return freq

result = count_orders(todays_orders)
print(result)