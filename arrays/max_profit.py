# LeetCode #121 - Best Time to Buy and Sell Stock
def max_profit(prices):
    # track the lowest price so far and the best profit seen
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0
    print(max_profit([5]))                 # 0
