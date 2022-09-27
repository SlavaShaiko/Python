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


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = 1
if a == b == c:
    d = d + 2
    print(d)
elif a == b or b == c or a == c:
    d = d + 1
    print(d)
else:
    d = d - 1
    print(d)
