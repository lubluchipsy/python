def merge(a, b):
    res = []
    while len(a) * len(b) > 0:
        if a[0] < b[0]:
            res.append(a.pop(0))
        else:
            res.append(b.pop(0))
    res.extend(a + b)
    return res

def merge_sort(a):
    if len(a) == 1:
        return a
    else:
        half = len(a) // 2
        return merge(merge_sort(a[:half]), merge_sort(a[half:]))
    
a = list(map(int, input().split()))
print(*merge_sort(a))

