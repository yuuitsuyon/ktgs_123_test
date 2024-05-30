# Условный оператор
# if Условие:
# Начало блока кода.
# Выполнится, если условие True.
# Один отступ вправо от уровня
# объявления условного оператора
# ...
# Конец блока кода
#else:
# Начало блока кода.
# Выполнится, если условие False.
# Один отступ вправо от уровня объявления условного оператора
# ...
# Конец блока кода
# Код который будет выполняться
# после условного оператора.
# Один отступ влево, чтобы закончить объявление циклa

is_rainy = True # дождь будет

if is_rainy:
    print('Беру зонт')
    print('Надеть сапоги')
else:
    print('Не беру зонт')
    print('Иду гулять')

is_rainy = False  # дождя не будет

if is_rainy:
    print('Беру зонт')
    print('Надеть сапоги')
else:
    print('Не беру зонт')
    print('Иду гулять')

is_rainy = True # дождь будет
heavy_rain = False # не сильный дождь

if is_rainy:
    if heavy_rain:
    print('Беру зонт')
else:
    print('Беру дождевик')
else:
print('Не беру зонт')
print('Иду гулять')
#
print("Пять больше трех?", 5 > 3) # True
print("Длина слова равна 1?", len("Hello") == 1) # False
print("7 не равно 12?", 7 != 12) # True

list_ = [1, 2, 3, 4, 5]

print("В списке есть число 7?", 7 in list_) # False
some_var = None
other_var = None
print(some_var is other_var) #True
#
example = (2 > 3) and (2 < 2) or (1 != 5) and (not (5 < 3) or (3 == 1))

my_result = False and False or True and (not False or False)
my_result = False and False or True and (True or False)
my_result = (False and False) or (True and True)
my_result = False or True
my_result = True

print(example)
print(my_result)
print(example == my_result)
#
str_1 = 'test'
str_2 = "test"
str_3 = '''test'''
str_4 = """test"""

print(str_1 == str_2 == str_3 == str_4)
print(
    (str_1 == str_2)
    and (str_2 == str_3)
    and (str_3 == str_4)
)

# Плохо
# if a > 10:
#     print('a больше 10')
# else:
#     if a < 10
#         print('a меньше 10')
#     else:
#         print('a равно 10')

# Хорошо
if a > 10:
    print('a больше 10')
elif a < 10:
    print('a меньше 10')
else:
    print('a равно 10')
