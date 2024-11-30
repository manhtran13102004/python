# 1
# the array isn't sorted

def find_all_index(nums, target, left, right):
    results = []
    if left > right:
        return []

    mid = (left + right) // 2
    if nums[mid] == target:
        results.append(mid)
        c1,c2 = mid-1, mid+1
        while c1 >= 0 and nums[c1] == target:
            results.append(c1)
            c1 -= 1
        
        while c2 < len(nums) and nums[c2] == target:
            results.append(c2)
            c2 += 1

    return results

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15
index_list = find_all_index(numbers, number_to_find, 0, len(numbers))
index_list.sort()
print(index_list    )