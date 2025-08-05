def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Bubble sorting : ",bubble_sort([87,25,81,95,36,74]))
print("Bubble sorting : ",bubble_sort([12,15,11,9,6,14]))