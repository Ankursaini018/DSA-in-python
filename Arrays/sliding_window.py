def  best_choclates(prices, window_size):
    current_total = sum(prices[0:window_size])
    best_total = current_total

    print(f"window1:{prices[0:window_size]} = {current_total}")

    for i in range(window_size, len(prices)):
        left_chocolate = prices[i-window_size]  
        right_choclate = prices[i]

        current_total = current_total - left_chocolate + right_choclate

        window = prices[i-window_size +1 : i+1]

        print(f"window: {window} = {current_total}")

        if current_total > best_total:
            best_total = current_total

    return best_total
prices = [2,4,6,1,7,3,5]
answer = best_choclates(prices,3)
print("best total", answer)   
