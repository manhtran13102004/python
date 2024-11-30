from random import randint

def find_pivot(nums):
    nums.sort()
    return nums[1]

def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i
    
def lomuto_qsort(nums, left, right):
    if left < right:
        print('Before partition:    ', nums)
        p = partition(nums, left, right)
        print(f'After partition at {p}:', nums)
        lomuto_qsort(nums, left, p-1)
        lomuto_qsort(nums, p+1, right)
    
def qsort(nums):
    if len(nums) <= 1:
        return nums
    pivot_index = find_pivot(nums[0], nums[len(nums)-1], nums[len(nums)//2])
    pivot = nums[pivot_index]
    left_arr = [x for x in nums[0:pivot_index] if x <= pivot] + [x for x in nums[p]]
    right_arr = [x for x in nums[1:] if x > pivot]
    return qsort(left_arr) + [pivot] + qsort(right_arr)

nums = [randint(1,100) for _ in range(15)]
lomuto_qsort(nums, 0, len(nums)-1)
print(nums)
# print(qsort(nums))
