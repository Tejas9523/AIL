def bubbleSort(arr):
    for i in range(len(arr)):
        temp = False

    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            temp = True

            if not temp:
                break


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print("Sorted arr in Ascending Order:")
print(data)
