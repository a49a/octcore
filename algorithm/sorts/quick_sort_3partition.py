def quick_sort_3partition(vec, left, right):
    if left >= right:
        return
    # i左边都是比pviot小的
    # j右边都是比pviot大的
    # cursor游标是需要和pviot比较的值

    cursor = left
    pivot = vec[left]
    i = left
    j = right
    while cursor <= j:
        if vec[cursor] < pivot:
            vec[cursor], vec[i] = vec[i], vec[cursor]
            i += 1
            cursor += 1
        elif vec[cursor] > pivot:
            vec[cursor], vec[j] = vec[j], vec[cursor]
            j -= 1
        else:
            cursor += 1

    quick_sort_3partition(vec, left, i - 1)
    quick_sort_3partition(vec, j + 1, right)

if "__main__" == __name__:
    unsorted = [4, 4, 4, 5, 3, 6, 2, 1]
    quick_sort_3partition(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
