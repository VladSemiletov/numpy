import numpy as np


'''В NumPy существует много способов создать массив.
Один из наиболее простых - создать массив из обычных списков
или кортежей Python, используя функцию numpy.array()
(запомните: array - функция, создающая объект типа ndarray)'''
a = np.array([1, 2, 3])
# print(a)
# print(type(a))
b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=complex)
# print(b)
'''Функция array() не единственная функция для создания массивов.
Обычно элементы массива вначале неизвестны, а массив, в котором
они будут храниться, уже нужен. Поэтому имеется несколько функций
для того, чтобы создавать массивы с каким-то исходным содержимым
(по умолчанию тип создаваемого массива — float64).

Функция zeros() создает массив из нулей,
а функция ones() — массив из единиц.
Обе функции принимают кортеж с размерами, и аргумент dtype'''
c = np.zeros((3, 5))
# print(c)
d = np.ones((2, 2, 2))
# print(d)
'''Функция eye() создаёт единичную матрицу (двумерный массив)'''
e = np.eye(5)
# print(e)
'''Функция empty() создает массив без его заполнения.
Исходное содержимое случайно и зависит от состояния
памяти на момент создания массива (то есть от того мусора,
что в ней хранится)'''
f = np.empty((3, 3))
# print(f)
'''Для создания последовательностей чисел,
в NumPy имеется функция arange(),
аналогичная встроенной в Python range(),
только вместо списков она возвращает массивы,
и принимает не только целые значения'''
g = np.arange(10, 30, 5)
# print(g)
'''Вообще, при использовании arange() с аргументами типа float,
сложно быть уверенным в том, сколько элементов будет получено
(из-за ограничения точности чисел с плавающей запятой).
Поэтому, в таких случаях обычно лучше использовать функцию linspace(),
которая вместо шага в качестве одного из аргументов принимает число,
равное количеству нужных элементов'''
h = np.linspace(0, 2, 9)
# print(h)
'''fromfunction(): применяет функцию ко всем комбинациям индексов'''


def f1(i, j):
    return i + j


k = np.fromfunction(f1, (3, 4))
# print(k)
