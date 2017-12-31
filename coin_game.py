# Python 2.7.1
# Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even.
# We play a game against an opponent by alternating turns.
# In each turn, a player selects either the first or last coin from the row, removes it from the row permanently,
# and receives the value of the coin.
# Determine the maximum possible amount of money we can definitely win if we move first.
# The opponent is as clever as the user.
# Description: https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
# Inputs should be lists of coin values.


# Returns the maximum amount of value in the coin game
def value(v):
    assert isinstance(v, list)
    n = v.__len__()
    if n < 2:
        return v[0]
    if n == 2:
        if v[0] >= v[1]:
            return v[0]
        else:
            return v[1]
    else:
        left = v[0] + min(value(v[1:n - 1]), value(v[2:n]))
        right = v[n - 1] + min(value(v[0:n - 2]), value(v[1:n - 1]))
        if left >= right:
            return left
        else:
            return right


# Returns the maximum value in the coin game and optimal strategies of both players.
# First character is the user's strategy and second character is the opponent's strategy.
# Number of coins i.e. length of the list should be even.
def game(v):
    assert isinstance(v, list)
    n = v.__len__()
    if n == 2:
        if v[0] >= v[1]:
            return v[0], ['LR']
        else:
            return v[1], ['RL']
    else:
        x, a = game(v[2:n])
        leftleft = v[0] + x
        y, b = game(v[1:n - 1])
        leftright = v[0] + y
        if leftleft <= leftright:
            left = leftleft
            which1 = ['LL'] + a
        else:
            left = leftright
            which1 = ['LR'] + b
        x, a = game(v[1:n - 1])
        rightleft = v[n - 1] + x
        y, b = game(v[0:n - 2])
        rightright = v[n - 1] + y
        if rightleft <= rightright:
            right = rightleft
            which2 = ['RL'] + a
        else:
            right = rightright
            which2 = ['RR'] + b
        if left >= right:
            return left, which1
        else:
            return right, which2


