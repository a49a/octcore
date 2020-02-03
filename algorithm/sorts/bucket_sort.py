DEFAULT_BUCKET_SIZE = 5


def bucket_sort(vec, bucket_size=DEFAULT_BUCKET_SIZE):
    if not vec:
        return vec
    min_v, max_v = min(vec), max(vec)
    bucket_count = (max_v - min_v) // (bucket_size + 1)
    buckets = [[] for _ in range(bucket_count + 1)]
    for x in vec:
        i = (x - min_v) // bucket_size
        buckets[i].append(x)
    r = []
    for x in buckets:
       r.extend(sorted(x))
    return r


if "__main__" == __name__:
    unsorted = [4, 3, 2]
    r = bucket_sort(unsorted)
    print(r)
