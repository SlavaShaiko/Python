# 1.Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).

# a = int(input("1"))
# b = int(input("2"))
# c = int(input("3"))
# arr = [a, b, c]
# count = [0, 0, 0]
# for i in range(3):
#    for j in range(3):
#        if arr[i] == arr[j]:
#           count[i] += 1
#            k = max(count)
# if k == 1:
#    print(0)
# else:
#    print(k)

# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))

# def GetNum(a, b, c):
#   if a == b == c:
#       return 3
#   if a == b or b == c or a == c:
#       return 2
#   return 0

# print(GetNum(a,b,c))


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = 1
# if a == b == c:
#     d = d + 2
#     print(d)
# elif a == b or b == c or a == c:
#     d = d + 1
#     print(d)
# else:
#     d = d - 1
#     print(d)

# 2.Даны два целых числа A и В, A>BA>B.
# Выведите все нечётные числа от A до B включительно,
# в порядке убывания. В этой задаче можно обойтись без инструкции if.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# b = b + (b + 1) % 2
# k = []
# for i in range(b, a + 1, 2):
#     k.append(i)
# k = k[::-1]
# print(*k)

# 3.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# n = int(input("введите число N: "))
# for i in range(n):
#     result = (-3) ** i
#     print(result, end=" ")

# 4.	Напишите программу, которая проверяет пятизначное число на палиндром.

# paltus = input("Введите число: ")
# if paltus[:2] == paltus[:2:-1]:
#     print("палиндром")
# else:
#     print("не палиндром")


# 5.	Удалить вторую цифру трёхзначного числа.
# a = 123
# print(a // 100 * 10 + a %10)

# 6.	Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# s = input("введите букавы: ")
# s1 = input("ведите букавы: ")
# print(s.count(s1))

sp = [11, 20, 43, 74, 95, 6, 7, 8]
print(sp[1:])  # кроме первого
print(sp[:-1])  # от начала до последнего
print(sp[::2])  # все четные индексы
print(sp[1::2])  # все нечетные индексы
print(sp[::-1])  # перевернутый
print(sp[-3 : len(sp)])  # последние 3
print(sp[-3:])  # последние 3
print(type(sp[-5:-1]))
print(type(sp[6]))
