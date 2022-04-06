def cyclic_rotation(a, k):
    if isinstance(a, list) and len(a) > 0:
        length = len(a)
        for n in range(k):
            copy = a.copy()
            a[0] = copy[length - 1]
            for i in range(length - 1):
                a[i + 1] = copy[i]
        return a
    else:
        print("the A is not an array or the length of the array is less than zero")


class CyclicRotation:
    pass
