
def max_profit(prices: list[int]) -> int:

    # simple implementation with sliding window that has O(n^2) complexity at worst case

    max_profit = float("-inf")
    
    for buy_idx in range(0, len(prices)):
       for sell_price in prices[buy_idx + 1:]:
           profit = sell_price - prices[buy_idx]
           if profit > max_profit:
               max_profit = profit
               
               
    return max_profit if max_profit > 0 else 0


def max_profit_improved(prices: list[int]) -> int:
    
    # improved implementation with O(n) complexity tracking a min price and max profit margin since we can greedily search for best profit
    
    max_profit = 0
    min_price = float("inf")
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        profit = price - min_price
            
        if profit > max_profit:
            max_profit = price - min_price
            
    return max_profit if max_profit > 0 else 0



               
       
if __name__ == "__main__":
    
    profit = max_profit([7, 1, 5, 3, 6, 4])
    print(profit)
    profit = max_profit_improved([7, 6, 4, 3, 1])
    print(profit)