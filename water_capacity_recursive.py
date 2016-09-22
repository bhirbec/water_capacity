
def water_capacity(arr):
    n = len(arr)
    pos, m = _find_max(arr, 0, n - 1)
    return _left_problem(arr, 0, pos - 1, m) + _right_problem(arr, pos + 1, n - 1, m)

def _left_problem(arr, start, end, m):
    if end <= start:
        return 0
    pos, new_m = _find_max(arr, start, end)
    return _left_problem(arr, start, pos - 1, new_m) + _capacity(arr, pos + 1, end, min(m, new_m))

def _right_problem(arr, start, end, m):
    if end <= start:
        return 0
    pos, new_m = _find_max(arr, start, end)
    return _right_problem(arr, pos + 1, end, new_m) + _capacity(arr, start, pos - 1, min(m, new_m))

def _capacity(arr, start, end, m):
    return sum(m - arr[i] for i in xrange(start, end + 1))

# Can we improve the way we search for the max?
def _find_max(arr, start, end):
    m = 0
    x = start
    for i in xrange(start, end+1):
        if arr[i] >= m:
            m = arr[i]
            x = i
    return x, m
