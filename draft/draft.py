
""" max = 0
for i in range(5):
    x = int(input())
    if max < x: max = x
print(max) """


""" n = int(input())
for i in range(-n, n + 1):
    print(i, end=' ') """


n = float(input())
n = (int(n*10)) % 10
if n == 0:
    print('нет')
else:
    print(n)
