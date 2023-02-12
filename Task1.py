# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degreeOf(z, step):
    if step == 1:
        return z
    elif step <0:
        print("Ошибка!")
        exit()
    else:

        return degreeOf(z, step - 1) * z


a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))
print(degreeOf(a, b))