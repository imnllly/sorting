from sortic import *

nums = []
comm = []
sort = []
num = 0
commands = ""
while (num != '!'):
    num = input()
    if num != '!':
        int(num)
        nums.append(num)
sort = nums.sort()
while (commands != '*'):
    commands = str(input())
    if commands != '*':
        comm = nums.commands()
print(comm)
if sort == comm:
    print("OK")
else:
    print("KO")
