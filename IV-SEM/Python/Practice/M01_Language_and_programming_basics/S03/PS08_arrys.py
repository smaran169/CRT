'''import numpy as np
nums =list(set(map(int,input().split())))
nums.sort()
if len(nums) >= 3:
    print(nums[-3])
else:
    print(max(nums))
'''
''' 
nums = list(map(int,input().split()))
inc = True
dec = True
 for i i  range(1,len(nums)):
   if nums[i] > nums[i-1]:
      dec = False
      if nums[i] < nums[i*1]:
      inc = False
      if inc or dec:
      print("Monotoic Array")
      else:
      print("non monotonic array")
      '''