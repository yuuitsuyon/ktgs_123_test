# 1
a, s, p = 1, 150, 200
while a <= 10:
    a += 2
    p += a
    s += p
    print(f'переменная s={s}')

#2способ
a, s, p = 1, 150, 200
while True:
    if a > 10:
        break
    a += 2
    p += a
    s += p
print(f'переменная s={s}')

# 2
S = 1
for n in range (1, 6):
    S *= n
print('Конец алгоритма')
print(f'Переменная s={s}')

# 3
m, n = 12, 5
while True:
    if m == n:
        break
    if m > n:
     m -= 2*n
    else:
     n -= 3
print('Конец алгоритма')
print(f'Переменная s={s}')
