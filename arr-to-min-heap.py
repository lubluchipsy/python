def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] > arr[l]:
        smallest = l

    if r < n and arr[smallest] > arr[r]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        heapify(arr, n, smallest)


arr = list(map(int, input().split()))
n = len(arr)
for i in range(n, -1, -1):
	heapify(arr, n, i)
print(arr)

