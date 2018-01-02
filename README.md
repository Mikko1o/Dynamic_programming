# Dynamic_programming
Dynamic programming algorithms

Maximum difference
# Compute the maximum L[j] - L[i] in a list, in which j > i
# The problem is well defined for list length at least 2

Maximum sublist - the sublist that has the maximum difference
# Find a sublist L[i .. j] which maximizes L[j] - L[i]
# For similar values of L[j] - L[i] the function returns the smallest possible sublist

Coin game
# Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even.
# We play a game against an opponent by alternating turns.
# In each turn, a player selects either the first or last coin from the row, removes it from the row permanently,
# and receives the value of the coin.
# Determine the maximum possible amount of money we can definitely win if we move first.
# The opponent is as clever as the user.
# Description: https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
# Inputs should be lists of coin values.

game(v)
# Returns the maximum value in the coin game and optimal strategies of both players.
# First character is the user's strategy and second character is the opponent's strategy.
# Number of coins i.e. length of the list should be even.

lcs(x, y)
# Returns the longest common subsequence of strings x and y

lcs_efficient(x, y)
# Returns the longest common subsequence
# A more efficient version that reduces the number of recursive calls
# Data structure "found" stores all the found common symbols -> only one recursive call results from one common symbol
# Please note: there are some bugs in this one, so at the moment this function does not work with all inputs
