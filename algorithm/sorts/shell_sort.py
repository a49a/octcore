def shell_sort(vec):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(vec)):
            need_insert_v = vec[i]
            j = i
            # 插入排序insertion sort
            while j >= gap and vec[j - gap] > need_insert_v:
                vec[j] = vec[j - gap]
                j -= gap
            vec[j] = need_insert_v
    return vec


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    r = shell_sort(unsorted)
    print(r)
