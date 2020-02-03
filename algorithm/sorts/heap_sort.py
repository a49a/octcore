def heapify(vec, parent_index, heap_size):
    largest_index = parent_index

    left_index = 2 * parent_index + 1
    right_index = 2 * parent_index + 2

    if left_index < heap_size and vec[left_index] > vec[largest_index]:
        largest_index = left_index
    if right_index < heap_size and vec[right_index] > vec[largest_index]:
        largest_index = right_index

    if largest_index != parent_index:
        vec[largest_index], vec[parent_index] = vec[parent_index], vec[largest_index]
        heapify(vec, largest_index, heap_size)


def heap_sort(vec):
    length = len(vec)

    # 构造大顶堆
    for i in range(length//2 - 1, -1, -1):
        heapify(vec, i, length)

    # 迭代交换，不断调整堆
    for i in range(length - 1, 0, -1):
        vec[0], vec[i] = vec[i], vec[0]
        heapify(vec, 0, i)

    return vec


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    r = heap_sort(unsorted)
    print(r)
