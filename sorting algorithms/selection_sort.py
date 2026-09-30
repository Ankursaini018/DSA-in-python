def selection_sort(prices):
    n = len(prices)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if prices[j]< prices[min_index]:
                min_index = j
        prices[i], prices[min_index] = prices[min_index], prices[i]
    return prices
prices = [850, 200, 520, 100, 430]
print(selection_sort(prices))
         