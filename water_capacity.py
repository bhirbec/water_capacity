
def water_capacity(arr):
    n = len(arr)
    if n == 0:
        return 0

    desc_arr = sorted(enumerate(arr), key=lambda item: -item[1])
    i_left, max_left = desc_arr[0]
    i_right, max_right = desc_arr[0]
    s = 0

    for k in xrange(1, n):
        i, new_max = desc_arr[k]
        if i_left < i < i_right:
            continue

        if i < i_left:
            s += _capacity(arr, i, i_left - 1, min(max_left, new_max))
            i_left, max_left = i, new_max
        else:
            s += _capacity(arr, i_right + 1, i, min(max_right, new_max))
            i_right, max_right = i, new_max

    return s

def _capacity(arr, start, end, m):
    return sum(m - arr[i] for i in xrange(start, end + 1))

