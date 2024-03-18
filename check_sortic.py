from func import *

nums = [] #добавленные числа(a)
empty = [] #типа b

num = 0
commands = ""
while (num != '!'):
    num = input()
    if num != '!':
        nums.append(int(num))

while (commands != '*'):
    commands = str(input())
    if commands != '*':
        if commands == "sa":
            nums = sa(nums)
        elif commands == "sb":
            empty = sb(empty)
        elif commands == "ss":
            nums, empty = ss(nums, empty)
        elif commands == "pa":
            nums, empty = pa(nums, empty)
        elif commands == "pb":
            nums, empty = pb(nums, empty)
        elif commands == "ra":
            nums = ra(nums)
        elif commands == "rb":
            empty = rb(empty)
        elif commands == "rr":
            nums, empty = rr(nums, empty)
        elif commands == "rra":
            nums = rra(nums)
        elif commands == "rrb":
            empty = rrb(empty)
        elif commands == "rrr":
            nums, empty = rrr(nums, empty)
        else:
            print("error")

sortn = sorted(nums)
print(nums)
if sortn == nums:
    print("OK")
else:
    print("KO")
