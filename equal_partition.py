# Partition a set S into S1 and S2 so that the sums of S1 and S2 are as equal as possible.


def sum(s):
    summa = 0
    for x in s:
        summa = summa + x
    return summa


def partition(s):
    n = s.__len__()
    if n > 3:
        x = s.pop()
        set1, set2 = partition(s)
        difference1 = abs(x + sum(set1) - sum(set2))
        difference2 = abs(sum(set1) - sum(set2) - x)
        if difference1 <= difference2:
            set1.add(x)
        else:
            set2.add(x)
        return set1, set2
    if n == 3:
        x = s.pop()
        y = s.pop()
        z = s.pop()
        difference1 = abs(x + y - z)
        difference2 = abs(y + z - x)
        difference3 = abs(x + z - y)
        if difference1 <= difference2 and difference1 <= difference3:
            print("d1")
            set1 = {x, y}
            set2 = {z}
        elif difference2 < difference1 and difference2 < difference3:
            print("d2")
            set1 = {y, z}
            set2 = {x}
        else:
            print("d3")
            set1 = {x, z}
            set2 = {y}
        return set1, set2
    if n == 2:
        x = s.pop()
        y = s.pop()
        return {x}, {y}
    else:
        return set(), set()

