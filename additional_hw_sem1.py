# ---------------------------------------------------------------------------------
# Задание 1
# ---------------------------------------------------------------------------------
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли
# этот день выходным
# print('Introduce what day of the week it is, using a number.\nExample: Monday - 1, Tuesday - 2, etc')
# a = int(input())
# if 0 > a > 71:
#     print('Introduce only numbers from 1 to 7!')
# else:
#     if a == 1:
#         print('Today is Monday!')
#     elif a == 2:
#         print('Today is Tuesday!')
#     elif a == 3:
#         print('Today is Wednesday!')
#     elif a == 4:
#         print('Today is Thursday!')
#     elif a == 5:
#         print('Today is Friday!')
#     elif a == 6:
#         print('Today is Saturday!')
#     elif a == 7:
#         print('Today is Sunday!')

# ---------------------------------------------------------------------------------
# Задание 2
# ---------------------------------------------------------------------------------
# Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)

# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((w and x)or(not y) or(not x == (not w))):
#                     print (x, y, z, w)
# Другой пример использования for с range
#r = range(2)
#for i in r:
#    print(i)

# Другой пример использования for с range
# for i in range(5):
#         print(i)

# Другой пример использования for со строками
#for i in 'qwerty':
#    print(i)

# ---------------------------------------------------------------------------------
# Задание 3
# ---------------------------------------------------------------------------------
# Напишите программу, которая принимает на вход
# координаты точки (X и Y), причем X!=0 и Y!=0,
# и выдает номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится)
# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# point = [x,y]
# if (x == 0 or y == 0):
#     print('X и Y не могут быть равны нулю!!!')
# else:
#     if x < 0 and y < 0:
#         print('Точка находится в левой нижней четверти.\n- -\no -')
#     if x < 0 and y > 0:
#         print('Точка находится в левой верхней четверти.\no -\n- -')
#     if x > 0 and y > 0:
#         print('Точка находится в правой верхней четверти.\n- о\n- -')
#     if x > 0 and y < 0:
#         print('Точка находится в правой нижней четверти.\n- -\n- о')





# ---------------------------------------------------------------------------------
# Задание 4
# ---------------------------------------------------------------------------------
# Напишите программу, которая по заданному номеру
# четверти, показывает диапазон возможных координат
# точек в этой четверти(x и y)

# quarter_number = int(input('Введите номер четверти(от 1 до 4): '))


# if quarter_number == 3:
#     print('Вы выбрали левую нижнюю четверть.\n- -\no -')
#     print('Диапазон:', '\nx = ', list(range(-10,0)), '\ny = ', list(range(-10,0)))
# elif quarter_number == 2:
#     print('Вы выбрали левую верхнюю четверть.\nо -\n- -')
#     print('Диапазон:', '\nx = ', list(range(-10,0)), '\ny = ', list(range(1,11)))
# elif quarter_number == 1:
#     print('Вы выбрали правую верхнюю четверть.\n- о\n- -')
#     print('Диапазон:', '\nx = ', list(range(1,11)), '\ny = ', list(range(1,11)))
# elif quarter_number == 4:
#     print('Вы выбрали правую нижнюю четверть.\n- -\n- о')
#     print('Диапазон:', '\nx = ', list(range(1,11)), '\ny = ', list(range(-10,0)))

# else:
#         print('Номер четверти должен быть не больше 4,\nно и не меньше 0. Попробуйте еще!')
    
#  Пример с match case:

# quarter = input()
# match quarter:
#     case "1":   
#         print("x > 0, y > 0")
#     case "2":
#         print("x < 0, y > 0")
#     case "3":
#         print("x < 0, y < 0")
#     case "4":
#         print("x > 0, y < 0")
#     case _:
#         print("error")




# ---------------------------------------------------------------------------------
# Задание 5
# ---------------------------------------------------------------------------------
# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние
# между ними в 2D пространстве
# import math
# x1 = int(input('Введите x1: '))
# y1 = int(input('Введите y1: '))
# point1 =[x1,y1]
# x2 = int(input('Введите x2: '))
# y2 = int(input('Введите y2: '))
# point2 = [x2,y2]

# print('Рассстояние между точками: ',math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# x_1 = int(input())
# y_1 = int(input())
# x_2 = int(input())
# y_2 = int(input())

# print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}") # после двоеточия
# :0.4 - это округление, после двоеточия начинается форматирование, мы можем использовать
# специальные формулы для манипулирования  полученными данными
# (отображение, размещение, смещение, f-строки)
# print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:.3f}") #вариант

