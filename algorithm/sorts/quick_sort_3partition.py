
def quick_sort_3partition(sorting, left, right):
    if right < left:
        return
    cursor = i = left
    j = right
    pivot = sorting[left]

    while cursor <= j:
        if sorting[cursor] < pivot:
            sorting[cursor], sorting[i] = sorting[i], sorting[cursor]
            cursor += 1
            i += 1
        elif sorting[cursor] > pivot:
            sorting[cursor], sorting[j] = sorting[j], sorting[cursor]
            j -= 1
        else:
            cursor += 1

    quick_sort_3partition(sorting, left, i - 1)
    quick_sort_3partition(sorting, j + 1, right)


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    quick_sort_3partition(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
