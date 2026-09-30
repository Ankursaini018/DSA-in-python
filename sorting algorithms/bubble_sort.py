def bubble_sort(prices):
    n = len(prices)
    for i in range(n):
        for j in range(0, n-i-1):
            if prices[j]>prices[j+1]:
                prices[j], prices[j+1] = prices[j+1], prices[j]
    return prices

prices = [850, 200, 520, 100, 430]
print(bubble_sort(prices))
