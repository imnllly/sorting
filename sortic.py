from func import *
num = 0
nums=[]
while (num != '!'):
    num = input()
    if num != '!':
        nums.append(int(num))
while (sorted(nums) != nums):
    if nums[1] > nums[2]:
        nums = sa(nums)
        print("sa")
    elif nums[1] <= nums[2]:
        nums = ra(nums)
        print("ra")
    elif reversed(nums) == sorted(nums):
        nums = ra(nums)
        print("ra")
    print()


