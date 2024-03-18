from func import *


def sort(a):
    n = len(a)
    while a != sorted(a)[::-1] or a != sorted(a):
        for i in range(n):
            if a == sorted(a)[::-1] or a == sorted(a):
                break
            for j in range(0, n - i - 1):
                if a == sorted(a)[::-1] or a == sorted(a):
                    break
                if a[j] > a[j + 1]:
                    a = sa(a)
                    print(a)
                    print("sa")
                    a = ra(a)
                    print(a)
                    print("ra")

                a = ra(a)
                print(a)
                print("ra")

a = []
num = None
while num != '!':
    num = input("Введите число или '!' для окончания ввода: ")
    if num != '!':
        a.append(int(num))
sort(a)
