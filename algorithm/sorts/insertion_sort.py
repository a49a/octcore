def insertion_sort(vec):
    for cursor in range(1, len(vec)):
        i = cursor
        while i > 0 and vec[i] < vec[i - 1]:
            vec[i], vec[i - 1] = vec[i - 1], vec[i]
            i -= 1
    return vec


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    r = insertion_sort(unsorted)
    print(r)