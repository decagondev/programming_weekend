#!/usr/bin/python

import sys
# denom = [2, 3, 4]

# making_change(20, [2])
#   making_change(11, [2, 3, 4, 5]) + making_change(20, [2, 3])


# def making_change(amount, denominations):
#     # base cases
#     if amount == 0:
#         return 1
#     if amount < 0:
#         return 0
#     if len(denominations) <= 0 and amount > 0:
#         return 0
#     # recursive case
#     else:
#         return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])

# with memoization
def making_change(amount, denominations, cache = dict()):
    # base cases
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) <= 0 and amount > 0:
        return 0
    
    # memoization cache case
    if (amount, len(denominations)) in cache.keys():
        return cache[(amount, len(denominations))]
    # recursive case
    else:
        waysToMakeChange = 0
        for i in range(len(denominations)):
            coin = denominations[i]
            if coin > amount:
                continue
            else:
                result = making_change(amount - coin, denominations[i:], cache)
                if result > 0:
                    waysToMakeChange += result
        
        cache[(amount, len(denominations))] = waysToMakeChange
        return waysToMakeChange



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")