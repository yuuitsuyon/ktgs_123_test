# Задача 1

str_ = "Строка с цифрой 1"

is_substr = "Строка" in str_ # True
print("В строке есть слово строка?", is_substr)

# Задача 2

number = 12
condition_1 = number % 2 == 0 # число кратно 2
condition_2 = number % 3 == 0 # число кратно 3

if condition_1 and condition_2:
    print('Число кратно 2 и 3')
else:
    print('Число не (кратно 2 и 3)')

# Задача 3

mount = 12
# символ \ позволит визуально разбить команду, для интерпретатора это одна строка
bad_condition = \
mount == 12 or \
    mount == 1 or \
    mount == 2 #Очень плохая запись условия

good_condition = mount in [12, 1, 2] #При множественном сравнении лучше использовать in

if good_condition:
    print("Зима!!!")

# Задача 4

hour = 7

bad_condition = (6 <= hour) and (hour < 12) # цепочки оператора всегда соединяются через AND
good_condition = 6 <= hour < 12

if good_condition:
    print("Утро!!!")

# Задача 5

list_ = [5, 6, 7, 8 , 9]

result = (4 in list_) and (8 in list_)
print(result)