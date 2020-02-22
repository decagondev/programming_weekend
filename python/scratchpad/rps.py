#!/usr/bin/python

import sys

"""
x = 2
bob:
    if x > 10:
        goto dave
    print("hello")
    add 1 to x
    goto bob

dave:

"""

def recursive_rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    def inner_function(rounds_left, result=[]):
        # base case
        if rounds_left == 0:
            outcomes.append(result)
            return
        
        # recursive case
        # run through all the plays
        for play in plays:
            # recursive call to inner_function(rounds_left - 1, result + [play]) 
            inner_function(rounds_left - 1, result + [play])

    inner_function(n, [])

    return outcomes
    
def rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    stack = []
    stack.append([])

    while len(stack) > 0:
        result = stack.pop()

        if n == 0 or len(result) == n:
            outcomes.append(result)
        else:  
            # recursive case
            # run through all the plays
            for play in plays:
                # append to out data structure (result + [play]) 
                stack.append(result + [play])

    return outcomes 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')