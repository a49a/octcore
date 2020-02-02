def bubble_sort(vec):
    length = len(vec)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if vec[j] > vec[j + 1]:
                swapped = True
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
        if not swapped:
            return vec
    return vec


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    sorted = bubble_sort(unsorted)
    print(sorted)
