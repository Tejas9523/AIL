def selectionSort(arr, size):
    for temp in range(size):
        index = temp

        for i in range(temp + 1, size):
            if arr[i] < arr[index]:
                index = i

        (arr[temp], arr[index]) = (arr[index], arr[temp])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print("Sorted arr in Ascending Order:")
print(data)
