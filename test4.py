#Create #tuple

a = (1, 1.2, 'hello')
a = {'a':1, 'b': 1.2, 'c': 'hello'}
a = (1, 1.1, 'a', [4, 5, 6], {'a':1, 'b':2}, None, True)
a = ()
b = tuple()
b = (1,)
a =
a = [1, 2.1, 3] #Раньше я был списком
tuple(a) # (1, 2.1, 3), но 'a' остался списком
b = tuple('abc') #('a', 'b', 'c')
a = [1, 2.1, 3] #это список list
tuple(a) # (1, 2.1, 3)
b = tuple('abc') #('a', 'b', 'c')
a = (1, 2.1, 'd') #в кортеже можно обращаться к элементу по индексу
a[0] #1
a[2] #'d'
a = (1, 1.1, 'a')
print(a) #(1, 1.1, 'a')
print((1, 1.1, 'a')) #(1, 1.1, 'a')
a = (1, 1.1, 'a')
a[0] #1
a[1] #1.1
a[2] #'a'
a[3] #Ошибка, вышли за границы
a[-1] #'a'
a[-2] #1.1
a[-3] #1
a[-4] #Ошибка, вышли за границы
a = (1, 2, 3)
b = (4, 5 , 6)
c = a+b
print(c) #(1, 2, 3, 4, 5, 6)
a += b #теперь "а" равно (1, 2, 3, 4, 5, 6)
a = (1, 2, 3)
b = 2
c = a*b
print(c) #(1, 2, 3, 1, 2, 3)
a *= b #теперь "а" равно (1, 2, 3, 1, 2, 3)
a = (1, 2, 3) #Это одномерный кортеж
b = ((1, 2 ,3), (4, 5 ,6), (7, 8 , 9)) #это двумерный (кортеж в кортеже) кортеж. Его можно представить как: ((1, 2, 3), (4, 5 ,6), (7, 8 , 9))
b = ((1, 2 ,3), (4, 5 ,6), (7, 8 , 9))
b[0] #Получение 1-го кортежа (1, 2, 3)
b[0][0] #получение 1-го элемента "1" из 1-го кортежа (1, 2, 3)
b[-1][-1] #получение последнего элемента "9" из последнего кортежа (7, 8, 9)
help(tuple) #информация о кортежах
a = (1, 2, 1)
a.count(1) #2. возвращает сколько раз в кортеже встретилось передаваемое значение. в примере вернется 2, так как в кортеже 2 единицы
a.index(2) #1. возвращает индекс, где передаваемое значение стоит в кортеже. в примере вернется 1, так как значение 2 в кортеже стоит на 1-ом индексе.
a = (1, 2, [1, 2, 3])
a[2][0] = 10 #теперь "а" (1, 2, [10, 2, 3]), так как внутри кортежа мы можем обратиться к изменяемому типу, хотя a[1] = 10 нам не позволит сделать.
a = [1, 2, 3] #создали список
b = (1, 2, a) #переделали "а" в кортеж. "b" = (1, 2, [1, 20, 3]). Но "а" это список, поэтому если изменить значение в "а", то оно автоматом поменяется на "b"
a[1] = 20 #теперь "а" равно [1, 20, 3]
print(b) #(1, 2, [1, 20, 3]), так как "а" это список, который внутри кортежа "b"
a = {'a':1} #словарь из 1 элемента (ключ "а", значение 1)
a = {'a':1, 'b':2} #словарь из 2 элементов (ключ "а", значение 1, ключ "b", значение 2)
a = dict([['a', 1], ['b', 2]]) #это создаст словарь {'a':1, 'b':2}
a = dict(1=1, b=2) #это создаст словарь {'a':1, 'b':2}
a = {} #это пустое множество
b = dict() #это пустой словарь
a = dict([['a', 1], ['b', 2]]) #передан список списков. это создаст словарь {'a':1, 'b':2}
a = dict((('a', 1], ['b', 2))) #передан кортеж кортежей. это создаст словарь {'a':1, 'b':2}
a = {1:'a', 1.1: 'b', 'c':3, (1,2):[1, 2, 3] frozenset({1, 2}): (1, 2), 4:{1:2, 3:4}, print: 4} #{1:'a', 1.1: 'b', 'c':3, (1,2):[1, 2, 3] frozenset({1, 2}): (1, 2), 4:{1:2, 3:4}, print: 4}, <built-in function print>: 4}
a = {'a':1, 'a':3, 'b':2} #{'a':1, 'a':3, 'b':2}. при одинаковых ключах - запишется то значение, которое объявлено последним
a = {'a':1, 'b':1.1}
print(a) #{'a':1, 'b':1.1}
print({'a':1, 'b':1.1}) #{'a':1, 'b':1.1}
a = {'a':1, 'b':1.2, 1:'abc'}
a[0] #будет ошибка, так как ключа 0 не существует в словаре
a['a'] #1
a['b'] #1.1
a[1] #'abc'
var_b = 'b'
a[var_b] #1.1 так как значение var_b = 'b'
a = {'a':1, 'b': 1.1, 1:'abc'}
a.get('a') #1
a.get(0) #None, если ключа не существует, то по умолчанию вернется None.
a.get(0, 'a') #'a'. если нет ключа, то вернется то, что было передано вторым.
a = {'a':1, 'b':1.5}
a.setdefault('c', 2)
a = {'a':1, 'b':1.5, 'c':2}
a = {'a':3, 'b':4}
a.update({'a':10, 'c':'dfe'})
a = {'a':10, 'b':4, 'c':'dfe'}
a = {'a':1, 'b': 1.1}
a['b'] =2
a = {'a':1, 'b':2}
a = {'a':1, 'b':1.1}
del a['a'] #теперь словарь а = {'b':1.1}
a = {'a':1, 'b':1.1} #это простой словарь
b = {'a':1, 'b': {'c':10}} #это вложенный словарь (словарь в словаре)
b = {'a':1, 'b':{'c':10}}
b['b'] #получение вложенного словаря {'c':10}
b['b']['c'] #получение 10 из{'c':10}
