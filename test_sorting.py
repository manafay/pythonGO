from sorting import selection_sort

print("Hello World")

def test_selection_sort():
    arr = [9,8,15,11,12,4,5,7,3,0]
    selection_sort(arr)
    assert arr == [0,3,4,5,7,8,9,11,12,15]
