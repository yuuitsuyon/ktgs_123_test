#Задача 1
empty_tuple = () # Пустой кортеж
tuple_with_one_item = (1,) # кортеж из одного элемента
tuple_ = (1, 2, "str")
print("Содержимое переменной empty_tuple:", empty_tuple,
type(empty_tuple))
print("Содержимое переменной tuple_with_one_item:",
tuple_with_one_item, type(tuple_with_one_item))
print("Содержимое переменной tuple_:", tuple_, type(tuple_))
list_ = [] # Пустой список
chars_list = ["a", "b", "c"]
print("Содержимое переменной list_:", list_, type(list_))
print("Содержимое переменной chars_list:", chars_list,
type(chars_list))
empty_string = "" # Пустая строка
str_ = "test" # Строковый тип данных
print("Содержимое переменной empty_string:", empty_string,
type(empty_string))
print("Содержимое переменной str_:", str_, type(str_))
empty_set = set() # Пустое множество
set_ = {3, 2, 1, 1} # Множество содержит в себе только
#уникальные элементы
print("Содержимое переменной empty_set:", empty_set,
type(empty_set))
print("Содержимое переменной set_:", set_, type(set_))
empty_dict = {} # Пустой словарь
dict_ = { # Словарь хранит пары ключ-значение. Ключи должны
#быть уникальными значениями
 "Имя": "Ваше имя",
 "Фамилия": "Ваша фамилия",
 "Возраст": 18,
 "Возраст": 20,}
print("Содержимое переменной empty_dict:", empty_dict,
type(empty_dict))
print("Содержимое переменной dict_:", dict_, type(dict_))

#Задача 2
list_players = ["Маша", "Петя", "Саша", "Оля",
"Кирилл"]
last_player = list_players[-1]
reestr = {"Первый участник": list_players[0]}
print("Последний участник:", last_player)
print("Первый участник:", reestr["Первый участник"])

#Задача 4
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
print(seasons_dict)

#Задача 5
users = ['user1', 'user2', 'user3', 'user1', 'user4',
'user2']
statistics = {'Общее количество': 0, 'Уникальные посещения': 0}
statistics['Общее количество'] = len(users)
statistics['Уникальные посещения'] = len(set(users))
print(statistics)

#Задача 6
numbers = [1, 2, 3, 1, 2, 5, 6, 7, 8, 1, 1, 2, 3, 4, -6, -4, -3, -2, - 1, -6, -5]
unique_numbers = set(numbers)
sum_of_numbers = sum(unique_numbers)
count_of_numbers = len(unique_numbers)
average_of_numbers = round(sum_of_numbers / count_of_numbers, 5)
describe = {"Сумма уникальных чисел:":
sum_of_numbers,
            "Количество уникальных чисел:":
count_of_numbers,
            "Среднее арифметическое уникальных чисел:": average_of_numbers,}
print(describe)

#Задача 1: первый и последний лыжник
list_participants = ["Орлов", "Петров", "Иванов", "Сидоров", "Васильев", "Черепахин"]
last_participant = list_participants[-1]
winner = {"Первый лыжник":
        list_participants[0]}
print(f"Последний участник: {last_participant}")
print(f"Первый участник: {winner['Первый лыжник']}")

#Задача 2: инвентаризация в библиотеке
sps_books = ["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон", "Ревизор", "Гранатовый браслет"]
last_book = sps_books[-1]
catalog = {"Пушкин": sps_books[0]}
print(f"Последняя книга: {last_book}")
print(f"Первая книга Пушкина: {catalog['Пушкин']}")

#Задача 3: покупки в интернет магазине
shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник", "Рюкзак", "Термос", "Миска", "Ветровка", "Коврик"]
unique_items = set(shopping_list)
count_unique_items = len(unique_items)
print(f"Количество уникальных товаров: {count_unique_items}")


