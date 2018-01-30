# Square root of an integer


# call this
def find_sqr(n):
    return bin_search(0, n, n)


# Recursive help function for finding the square root
def bin_search(start, end, x):
    mid = (start + end) / 2
    a = mid * mid
    b = (mid + 1) * (mid + 1)
    if a == x:
        return mid
    elif a < x < b:
        return mid
    elif a < x:
        return bin_search(mid + 1, end, x)
    elif a > x:
        return bin_search(start, mid - 1, x)

