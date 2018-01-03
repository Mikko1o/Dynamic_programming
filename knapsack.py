# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
# knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
# associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the
# maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.


# Computes the maximum value in the given instance.
# Input should be (values, weights, capasity). Values and weights should be in lists.
def knapsack(v, w, c):
    assert isinstance(v, list)
    assert isinstance(w, list)
    n = v.__len__()
    if n == 1:
        if w[0] <= c:
            return v[0]
        else:
            return 0
    item_value = v.pop()
    item_weight = w.pop()
    possibility1 = 0
    if item_weight <= c:
        possibility1 = knapsack(v, w, c - item_weight) + item_value
    possibility2 = knapsack(v, w, c)
    return max(possibility1, possibility2)

