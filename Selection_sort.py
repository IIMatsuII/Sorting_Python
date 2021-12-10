def find_min(arr, start, end):
    minimum = arr[start]
    min_idx = start
    for idx in range(start, end):
        if arr[idx] < minimum:
            minimum = arr[idx]
            min_idx = idx
    return min_idx

def selection_sort(arr):
    i = 0
    arr_size = len(arr)
    while i < arr_size:
        min_idx = find_min(arr, i, arr_size)
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        i+=1
    return arr

a = [12, 5, 90, 4, 22, 34, 57, 78]
print(selection_sort(a))