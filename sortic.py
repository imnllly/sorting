from func import *
from colorama import *


def sort(a, b):
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[0] > a[1]:
                a = sa(a)
                # print(a)
                print(Fore.BLUE + "sa")
            a = ra(a)
            # print(a)
            print(Fore.LIGHTBLUE_EX +"ra")
        a, b = pb(a, b)
        # print(a)
        #print(b)
        print(Fore.CYAN + "pb")

b = []
a = []
num = None
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
sort(a, b)
