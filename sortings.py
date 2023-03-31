# отсортирован ли массив
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return False
    return True

# сортировка вставками
def insertion_sort(a):
    b = a.copy()

    for k in range(len(b) - 1):
        for i in range(k + 1):
            if b[k-i+1] < b[k-i]:
                b[k-i], b[k-i+1] = b[k-i+1], b[k-i]
            else:
                break
    return b

# сортировка пузырьком
def bubble_sort(a):
    b = a[:]
    n = len(b)

    for i in range(0, n-1):
        if is_sorted(b):
            break
        for j in range(0, n-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
    return b

# сортировка выбором
def selection_sort(a):
    for i in range(0, len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

import time

a = list(map(int, input().split()))

start = time.perf_counter()
bubble_sort(a)
end = time.perf_counter()
print('Сортировка пузырьком:', end - start)
#Подсчет времени

start = time.perf_counter()
insertion_sort(a)
end = time.perf_counter()
print('Сортировка вставкой:', end - start)
#Подсчет времени

start = time.perf_counter()
selection_sort(a)
end = time.perf_counter()
print('Сортировка выбором:', end - start)
#Подсчет времени

# У сортировки пузырьком в худшем и среднем случаях сложность O(n^2), в лучшем - О(n)
# у сортировки выбором - О(n^2) в лучшем, худшем и среднем случаях
# у сортировки вставками в худшем и среднем случаях сложность O(n^2), в лучшем - О(n)
