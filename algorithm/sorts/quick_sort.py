def quick_sort(vec):
    if len(vec) <= 1:
        return vec
    pviot = vec.pop()
    greater, lesser = [], []
    for x in vec:
        if x > pviot:
            greater.append(x)
        else:
            lesser.append(x)
    return quick_sort(lesser) + [pviot] + quick_sort(greater)


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    r = quick_sort(unsorted)
    print(r)
