def insertionSort(arr):
    for temp in range(1, len(arr)):
        key = arr[temp]
        j = temp - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print("Sorted arr in Ascending Order:")
print(data)
