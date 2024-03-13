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
            sa(nums)
        elif commands == "sb":
            sb(empty)
        elif commands == "ss":
            ss(nums, empty)
        elif commands == "pa":
            pa(nums, empty)
        elif commands == "pb":
            pb(nums, empty)
        elif commands == "ra":
            ra(nums)
        elif commands == "rb":
            rb(empty)
        elif commands == "rr":
            rr(nums, empty)
        elif commands == "rra":
            rra(nums)
        elif commands == "rrb":
            rrb(empty)
        elif commands == "rrr":
            rrr(nums, empty)
        else:
            print("error")
print(nums)
print(sorted(nums))
if sorted(nums) == nums:
    print("OK")
else:
    print("KO")
