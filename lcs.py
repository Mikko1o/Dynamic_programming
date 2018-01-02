# Python 2.7.1
# Find the longest common subsequence of two strings


# Returns the longest of two strings
def maximum(x, y):
    if x.__len__() >= y.__len__():
        return x
    else:
        return y


# Returns the longest common subsequence
def lcs(x, y):
    assert isinstance(x, str)
    assert isinstance(y, str)
    n = x.__len__()
    m = y.__len__()
    if n == 0 or m == 0:
        return ""
    S1 = ""
    i = 0
    for c in x:
        if c == y[0]:
            S1 = c + lcs(x[i+1:n], y[1:n])
            break
        i = i + 1
    S2 = lcs(x, y[1:n])
    return maximum(S1, S2)


# Returns the longest common subsequence
# A more efficient version that reduces the number of recursive calls
# Data structure "found" stores all the found common symbols -> only one recursive call results from one common symbol
# Please note: there are some bugs in this one, so at the moment this function does not work with all inputs
def lcs_efficient(x, y):
    assert isinstance(x, str)
    assert isinstance(y, str)

    found = set()

    def inner_function(a, b, ai, bi):
        n = a.__len__()
        m = b.__len__()
        if n == 0 or m == 0:
            return ""
        s1 = ""
        i = 0
        for c in a:
            if c == b[0]:
                if found.__contains__((ai + i, bi)):
                    break
                else:
                    found.add((ai + i, bi))
                    s1 = c + inner_function(a[i + 1:n], b[1:n], ai + i + 1, bi + 1)
                    break
            i = i + 1
        if m > 1:
            s2 = inner_function(a, b[1:n], ai, bi + 1)
        else:
            s2 = ""
        if s1.__len__() >= s2.__len__():
            return s1
        else:
            return s2

    return inner_function(x, y, 0, 0)

