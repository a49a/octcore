def selection_sort(vec):
    length = len(vec)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if vec[min_index] > vec[j]:
                min_index = j
        if min_index != i:
            vec[i], vec[min_index] = vec[min_index], vec[i]


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    selection_sort(unsorted)
    print(unsorted)