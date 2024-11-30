def inserted(nums, val):
    
    i = 0
    while i < len(nums) and nums[i] < val:
        i += 1
    
    return nums[:i] + [val] + nums[i:]

def median(nums):
    if nums == []:
        return None
    n = len(nums)
    return nums[n//2] if n % 2 == 1 else (nums[n//2] + nums[(n-1)//2])/2
a = []
while True:
    x = int(input())
    a = inserted(a, x)
    print(a)
    print('median: ',median(a))