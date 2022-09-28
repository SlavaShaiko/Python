# Задайте список из N элементов, заполненных числами из промежутка [-N, N]
# (например, [-3, -2, 1, 0, 1, 2, 3].
# Найдите произведение элементов на указанных позициях.

from array import array
from random import randint
n = int(input('Введите длину массива: '))
array = []
for i in range(n):
    array.append(randint(-10, 10))
print(array)

index_1 = int(input('Введите позицию первого элемента: '))
index_2 = int(input('Введите позицию второго элемента: '))

for i in range(len(array)):
    composition = array[index_1 - 1]*array[index_2 - 1]
print(
    f'Произведение элементов на указанных позициях: {array[index_1 -1]} * {array[index_2 -1]}', composition)
