#    int,float,boolean,str,list,None

# value = None
# a = 123
# b = 1.23456
# print(type(a))
# print(type(b))
# value = 1234
# print(value)
# s = 'sdfsd'
# print(a, b, value, s)
# print(a, '-', b, '-', value, '-', s)
# print('{1} - {2} - {0} - {3}'.format(a, b, value, s))
# print(f'{a} - {b} - {value} - {s}')

# list = ['1', '54', 2.34, 23, '4', 5]
# print(list)

# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)
# print('{} -- {}'.format(a, b))

# -----------------------------------------------------------------------
# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций**, ⊕, ⊖, *, /, //, %, +, -
# () Скобки меняют приоритет

# a = 12
# b = 4
# c = a+b
# print(c)

# a = 12
# b = 4
# c = a-b
# print(c)

# a = 12
# b = 4
# c = a*b
# print(c)

# a = 12
# b = 4
# c = a/b
# print(c)

# a = 12
# b = 4
# c = a//b
# print(c)

# a = 12
# b = 4
# c = a % b
# print(c)

# a = 12
# b = 4
# c = a**b
# print(c)

# a = 12.78
# b = 4
# c = a**b
# print(c)

# a = 12.78
# b = 4
# c = round(a**b)
# print(c)

# a = 12.7845
# b = 4
# c = round(a**b, 5)
# print(c)

# a = 5
# a += 5
# print(a)

# --------------------------------------------------------

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 > 1
# print(a)

# a = 'asd'
# b = 'asd'
# print(a == b)

# a = 1 < 2 < 4
# print(a)

# a = int(input('a='))
# b = int(input('b='))
# if a > b:
# print('a>b')
# else:
#  print('b>a')

# if---------------------------------------------

# username = input('Введите имя: ')
# if username == 'Маша':
# print('Ура, это же МАША!')
# elif username == 'Марина':
# print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
# print('Ильнар - топ)')
# else:
# print('Привет, ', username)

# while-------------------------------------------

# original = 233457
# inverted = 0
# while original != 0:
# inverted = inverted * 10 + (original % 10)
# original //= 10
# print(inverted)

# original = 233457
# inverted = 0
# while original != 0:
# inverted = inverted * 10 + (original % 10)
# original //= 10
# print(original)
# else:
# print('Пожалуй')
# print('хватит )')
# print(inverted)
# Пожалуй
# хватит )
# 32

# for----------------------------------------------

# for i in 1, 2, 3, 4, 5:
# print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#   print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#   print(i)

# r = range(10)
# for i in r:
#   print(i)

# help(int)

# Немного о строках-------------------------------------

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
#print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
# print(c)

# Списки: введение-----------------------------------

#numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
#numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
#numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#   i *= 2
#  print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]


#colors = ['red', 'green', 'blue']
# for e in colors:
# print(e) # red green blue
# for e in colors:
# print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемен

# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1))  # Целое
print(f(2.3))  # 23
print(f(28))  # None
print(type(f(1)))  # str
print(type(f(2.3)))  # int
print(type(f(28)))  # NoneTyp
