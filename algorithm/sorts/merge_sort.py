def merge_sort(vec):
    if len(vec) <= 1:
        return vec
    mid = len(vec) // 2
    return merge(merge_sort(vec[:mid]), merge_sort(vec[mid:]))


def merge(left, right):
    r = []
    while left and right:
        r.append((left if left[0] < right[0] else right).pop(0))
    return r + left + right


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    r = merge_sort(unsorted)
    print(r)
