# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
# such that all elements of the subsequence are sorted in increasing order.
# Description of the problem: https://www.geeksforgeeks.org/longest-increasing-subsequence/


# Returns the lengths of longest increasing subsequences up to every element in a list
# List "lengths" stores the length of the LIS up to that index
# lengths[j] = max {lengths[i] + 1}, on the condition a[i] < a[j]
def lengths_of_lis(a):
    assert isinstance(a, list)
    lenghts = [0] * a.__len__()
    for j, v in enumerate(a):
        i = 0
        maximum = 0
        while i < j:
            if a[i] < a[j]:
                if lenghts[i] > maximum:
                    maximum = lenghts[i]
            i = i + 1
        lenghts[j] = maximum + 1
    return lenghts


# Returns a longest increasing subsequence
# Finds a sequence by traceback from the lenghts of longest increasing subsequences
def lis(a):
    assert isinstance(a, list)
    if a.__len__() == 0:
        return []
    lenghts = lengths_of_lis(a)
    start_value = 0
    for i, v in enumerate(lenghts):
        if v > start_value:
            start_value = v
            start_index = i
    value = start_value
    index = start_index
    subsequence = [a[start_index]]
    while value > 1:
        while not lenghts[index] == value - 1:
             index = index - 1
        value = lenghts[index]
        subsequence.append(a[index])
    subsequence.reverse()
    return subsequence

