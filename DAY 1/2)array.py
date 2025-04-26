# 🧮 Problem 2: Best Time to Buy and Sell Stock (Easy)
# 📌 LeetCode #121
# 🔗 Best Time to Buy and Sell Stock – LeetCode

# ❓ Problem Statement:
# You are given an array prices where prices[i] is the price of a stock on the i-th day.

# You want to buy one stock and sell one stock, but must buy before selling.

# Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

prices = [7, 1, 5, 3, 6, 4]
# max_profit = 0

# for i in range(len(prices)):
#     for j in range(i + 1, len(prices)):
#         profit = prices[j] - prices[i]  # Buy at i, sell at j
#         if profit > max_profit:
#             max_profit = profit

# print(max_profit)


#OPTIMIZED CODE 
min_price = float('inf')
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
print(max_profit)
