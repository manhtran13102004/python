

def merge(arr, num1, num2, key, descending):
    i = j = k = 0
    comparator = (lambda a, b: a >= b) if descending else (lambda a, b: a <= b)
    
    while i < len(num1) and j < len(num2):
        if comparator(num1[i][key], num2[j][key]):
            arr[k] = num1[i]
            i += 1
        else:
            arr[k] = num2[j]
            j += 1
        k += 1

    # Gộp phần còn lại
    arr[k:] = num1[i:] + num2[j:]

    
def merge_sort(arr, key, descending=False):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left, key, descending)
    merge_sort(right, key, descending)
    
    print('before: ', arr)
    merge(arr, left, right, key, descending)
    print('after: ', arr)


from random import randint

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
merge_sort(elements, key='time_hours', descending=True)

for element in elements:
    print(element)
