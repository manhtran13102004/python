def ssrd(nums):
    n = len(nums)
    if n <= 1:
        return
    
    gap = n//2
    while gap > 0:
        i = gap
        while i < len(nums):
            need_insert = nums[i]
            j = i
            while j-gap >= 0 and nums[j-gap] > need_insert:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = need_insert
            if j > 0 and nums[j-1] == nums[j]:
                del nums[j]
            else:
                i += 1
        gap //= 2
    
from random import randint

a = [randint(1, 20) for _ in range(20)]
print(a)
ssrd(a)
print(a)