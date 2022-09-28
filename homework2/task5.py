# Реализуйте алгоритм перемешивания списка
# (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

from random import randint

n = int(input('Введите длину списка: '))
list_original = []
for i in range(n):
    list_original.append(randint(-10, 10))
print('Исходный список:', list_original)

def mix_list(list):
    list = list[:]
    list_length = len(list)
    for i in range(list_length):
        index_ran = randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_ran]
        list[index_ran] = temp
    return list

mixed_list = mix_list(list_original)

print('Перемешанный список:', mixed_list)
