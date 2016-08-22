def min_index(arr, startIndex, stopIndex):
    mi = startIndex
    i = startIndex + 1
    while i < len(arr):
        if(arr[i] < arr[mi]):
            mi = i
        i += 1
    return mi


def selection_sort(arr):
    i = 0
    while i < len(arr) - 1:
        mi = min_index(arr, i, len(arr))
        arr[i], arr[mi] = arr[mi], arr[i]
        i += 1
