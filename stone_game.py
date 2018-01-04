# Two players are playing a game with n stones where player 1 always plays first. The two players move in alternating
# turns and plays optimally. In a single move a player can remove either 1, 3 or 4 stones from the pile of stones.
# If a player is unable to make a move then that player loses the game. Given the number of stones where n is less than
# equal to 200, find and print the name of the winner.


# The solution here is to create an array of game outcomes until given n.
# The player makes the first move, the opponent the second.
# (The array repeats the same pattern over and over again, so this is not the simplest possible solution.)
def game_of_stones(n):
    assert isinstance(n, int)
    if n < 0 or n > 200:
        return "invalid number"
    if n == 0 or n == 2:
        return "opponent"
    if n == 1 or n == 3 or n == 4:
        return "player"
    i = 5
    results = ['o', 'p', 'o', 'p', 'p']
    while i <= n:
        if results[i-1] == 'o' or results[i-3] == 'o' or results[i-4] == 'o':
            results.append('p')
        else:
            results.append('o')
        i = i + 1
    if results[n] == 'p':
        return "player"
    else:
        return "opponent"


# Faster algorithm for the same game
# The results of the game repeat the following pattern "O P O P P P P" starting from zero.
# If n mod 7 == 0 or 2, the player loses. Otherwise the player wins.
# This is the simplest solution for the game.
def game_fast(n):
    assert isinstance(n, int)
    if n < 0:
        return "invalid number"
    if n % 7 == 0 or n % 7 == 2:
        return "opponent"
    else:
        return "player"

