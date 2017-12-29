# Python 2.7.1
# Algorithms for maximum difference in a list and a maximum sublist
# Lists should contain only numbers


# Compute the maximum L[j] - L[i] in a list, in which j > i
# The problem is well defined for list length at least 2
def max_difference(L):
    assert isinstance(L, list)
    n = L.__len__()
    if n < 2:
        return L
    if n == 2:
        return L[1] - L[0]
    mid = n / 2
    if n == 3:
        return max(L[2]-L[1], L[2]-L[0], L[1]-L[0])
    else:
        difference1 = max(L[mid: n]) - min(L[0: mid])
        difference2 = max_difference(L[0: mid])
        difference3 = max_difference(L[mid: n])
    return max(difference1, difference2, difference3)


# Find a sublist L[i .. j] which maximizes L[j] - L[i]
# For similar values of L[j] - L[i] the function returns the smallest possible sublist
def max_sublist(L):
    assert isinstance(L, list)
    n = L.__len__()
    if n < 3:
        return L
    if n == 3:
        difference1 = L[2] - L[0]
        difference2 = L[2] - L[1]
        difference3 = L[1] - L[0]
        # maximum sublist is L[0..2]
        if difference1 > difference2 and difference1 > difference3:
            return L
        # maximum sublist is L[0..1]
        if difference3 >= difference1 and difference3 >= difference2:
            return L[0:2]
        # maximum sublist is L[1..2]
        else:
            return L[1:3]
    else:
        mid = n / 2
        maximum = float("-inf")
        minimum = float("inf")
        index_min = -1
        index_max = -1
        for i, x in enumerate(L[0:mid]):
            if x < minimum:
                minimum = x
                index_min = i
        for i, x in enumerate(L[mid:n]):
            if x > maximum:
                maximum = x
                index_max = i
        difference1 = maximum - minimum
        L2 = max_sublist(L[0:mid])
        L3 = max_sublist(L[mid:n])
        difference2 = L2[L2.__len__() - 1] - L2[0]
        difference3 = L3[L3.__len__() - 1] - L3[0]
        if difference1 > difference2 and difference1 > difference3:
            return L[index_min: mid + index_max+1]
        if difference3 >= difference1 and difference3 >= difference2:
            return L3
        else:
            return L2
