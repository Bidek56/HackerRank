'''
A stock investor knows what the stock price of a certain stock will be for each of the future N days. 
The investor has an array of positive integers with each array element representing the stock price each day. 
Each day, the investor can take 1 of these actions:
1. do nothing
2. buy a single share of this stock 
3. sell any number of shares from the existing holdings (up to existing holdings only, cannot go into short-selling)

What is the maximum profit the investor can get?
Examples:
[1, 2, 3]: buy 1 share, buy 1 share, sell 2 shares at $3 per share 
[4, 3, 2]: do nothing
[5, 7, 1, 2]: buy 1 share at $5, sell 1 share at $7, buy 1 share at $1, sell one share at $2
'''

def maxprofit(prices: List[int]) -> int: 
    
    profit = 0
    for i, price in enumerate(prices):
        
        if i == len(price):
            return profit
        
        if price > price[i+1] and price[i+1] > price[i+2]:
            return profit
            
        if price >= price[i+1]:
            profit = profit + price
        elif price <= price[i+1]:
            profit = profit - price

    return profit
