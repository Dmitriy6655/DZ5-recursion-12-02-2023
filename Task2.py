# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
#
# 2 2
# 4

def sum(A, B, i=0):
    if B == 0:
        return 2 * i + A
    elif A == 0:
        return 2 * i + B
    else:
        return sum(A - 1, B - 1, i=i + 1)

a = int(input("Введите число A: "))
b = int(input("Введите число Б: "))

print("Сумма =", sum(a, b))
