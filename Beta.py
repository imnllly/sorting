from func import *


def sort(a):
    n = len(a)
    while a != sorted(a) and a != sorted(a)[::-1]:
        for i in range(n):
            if a == sorted(a) or a == sorted(a)[::-1]:
                break
            for j in range(0, n - i - 1):
                if a == sorted(a) or a == sorted(a)[::-1]:
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
