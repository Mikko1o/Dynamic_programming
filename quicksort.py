# Quicksort function using the last element as pivot


def partition(a, x):
    assert isinstance(a, list)
    left = []
    right = []
    for i in a:
        if i <= x:
            left.append(i)
        else:
            right.append(i)
    return left, right


def quicksort(a):
    assert isinstance(a, list)
    n = a.__len__()
    if n < 3:
        if n == 2:
            if a[0] <= a[1]:
                return a
            else:
                return [a[1], a[0]]
        if n < 2:
            return a
    part_elem = a.pop()
    left, right = partition(a, part_elem)
    return quicksort(left) + [part_elem] + quicksort(right)


print(quicksort([0, 1]))

print(quicksort([2, -6]))

print(quicksort([5, 4, 3, 0, 1, 0, 1, 0, 5, -2]))