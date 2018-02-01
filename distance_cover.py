# This function computes the number of ways to cover a given distance using steps 1, 2 or 3.


def dist_cover(l):
    assert isinstance(l, int)
    if l < 0:
        return -1
    number_of_ways = [1, 1, 2, 4]
    if l < 4:
        return number_of_ways[l]
    else:
        x = 4
        while x <= l:
            new_number = number_of_ways[x - 1] + number_of_ways[x - 2] + number_of_ways[x - 3]
            number_of_ways.append(new_number)
            x = x + 1
        return number_of_ways.pop()

