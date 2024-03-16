from func import *


def sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                ss(a, [])
                print("ss")
            ra(a)
            print("ra")

a = []
num = None
while num != '!':
    num = input("Введите число или '!' для окончания ввода: ")
    if num != '!':
        a.append(int(num))
sort(a)
