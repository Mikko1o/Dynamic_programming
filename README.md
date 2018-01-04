# Dynamic_programming
Dynamic programming algorithms

# Maximum difference
Compute the maximum L[j] - L[i] in a list, in which j > i
The problem is well defined for list length at least 2

# Maximum sublist - the sublist that has the maximum difference
Find a sublist L[i .. j] which maximizes L[j] - L[i]
For similar values of L[j] - L[i] the function returns the smallest possible sublist

# Coin game
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even.
We play a game against an opponent by alternating turns.
In each turn, a player selects either the first or last coin from the row, removes it from the row permanently,
and receives the value of the coin.
Determine the maximum possible amount of money we can definitely win if we move first.
The opponent is as clever as the user.
Description: https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
Inputs should be lists of coin values.

# game(v)
Returns the maximum value in the coin game and optimal strategies of both players.
First character is the user's strategy and second character is the opponent's strategy.
Number of coins i.e. length of the list should be even.

# Longest common subsequence
lcs(x, y)
Returns the longest common subsequence of strings x and y

lcs_efficient(x, y)
Returns the longest common subsequence
A more efficient version that reduces the number of recursive calls
Data structure "found" stores all the found common symbols -> only one recursive call results from one common symbol
Please note: there are some bugs in this one, so at the moment this function does not work with all inputs

# Longest increasing subsequence
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order.
Description of the problem: https://www.geeksforgeeks.org/longest-increasing-subsequence/

lengths_of_lis(a)
Returns the lengths of longest increasing subsequences up to every element in a list
List "lengths" stores the length of the LIS up to that index
lengths[j] = max {lengths[i] + 1}, on the condition a[i] < a[j]

lis(a)
Returns a longest increasing subsequence
Finds a sequence by traceback from the lenghts of longest increasing subsequences

# Stone game
Two players are playing a game with n stones where player 1 always plays first. The two players move in alternating turns and plays optimally. In a single move a player can remove either 1, 3 or 4 stones from the pile of stones. If a player is unable to make a move then that player loses the game. Given the number of stones where n is less than equal to 200, find and print the name of the winner.

game_of_stones(n)
The solution here is to create an array of game outcomes until given n. The player makes the first move, the opponent the second. (The array repeats the same pattern over and over again, so this is not the simplest possible solution.)

game_fast(n)
Faster algorithm for the same game The results of the game repeat the following pattern "O P O P P P P" starting from zero. If n mod 7 == 0 or 2, the player loses. Otherwise the player wins.
This is the simplest solution for the game.

# Knapsack
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.

knapsack(v, w, c)
Computes the maximum value in the given instance.
Input should be (values, weights, capasity). Values and weights should be in lists.
