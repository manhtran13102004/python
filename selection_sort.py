def comparator(element1, element2, categories):
    for category in categories:
        if element1[category] == element2[category]:
            continue
        return element1[category] < element2[category]
    return True

def selection_sort(ori_arr, categories):
    n = len(ori_arr)
    arr = ori_arr[:]
    for i in range(n):
        min_ = i
        for j in range(i+1, n):
            if comparator(arr[j], arr[min_], categories):
                min_ = j
        arr[i], arr[min_] = arr[min_], arr[i]
    return arr


a = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
categories = ['First Name', 'Last Name']
b = selection_sort(a, categories)
for element in b:
    print(element)