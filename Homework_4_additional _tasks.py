#===================================================================================
# Задачи на повторение по материалам предыдущих семинаров (по желанию)
#===================================================================================

# Задача 101.
#---------------------------------------------------------------------------------
# Вычислить число π c заданной точностью d
# 3,14159265358
# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

# РЕШИЛА! Длинно, но правильно!
# не добавила условие-ограничитель, было лень,можно через if/else
# pi = 3.14159265358
# n = float(input('Введите число: '))
# count = 0
# while n < 1:
#     n = n *10
#     count +=1
# # print(count)
# for i in range(count):
#     pi = pi *10
# # print(pi)
# int_pi = int(pi)
# float_pi = float(int_pi)
# # print(int_pi)
# # print(float_pi)
# for i in range(count):
#     float_pi = float_pi / 10
# print(round(float_pi,count))




# НЕ ПОНИМАЮ УСЛОВИЕ!!!
# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#---------------------------------------------------------------------------------

# n = int(input('Introduce an integer: '))









# НЕ ПОНИМАЮ УСЛОВИЕ!!!
# Задача 103.
#---------------------------------------------------------------------------------
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2 

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0


# НЕ РЕШИЛА!!!! Пока не решу предыдущие 2 задачи, нет смыслы делать эту
# Задача 104.
#---------------------------------------------------------------------------------
# Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена
# (полученные в результате работы программы из задачи 103). Необходимо сформировать файл file_sum.txt,
# содержащий сумму многочленов.



# Задача 105.
#---------------------------------------------------------------------------------
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#РЕШИЛА!!!
#Если правильно поняла условие

# stroka = 'Напишите программу, удаляющую из текста все слова, содержащие "абв".'
# list_stroka = stroka.split()
# print(list_stroka)
# for i in range(len(list_stroka)):
#     if 'в' in list_stroka[i]:
#         list_stroka[i] = ''
#     if 'а' in list_stroka[i]:
#          list_stroka[i] = ''
#     if 'б' in list_stroka[i]:
#         list_stroka[i] = ''
# print(list_stroka)
# new_stroka = ''
# for i in list_stroka:
#     new_stroka = new_stroka + ' ' + i
# print(new_stroka)








# Задача 106.
#---------------------------------------------------------------------------------
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)
# 
#НЕ РЕШИЛА, нужно продумать алгоритм
# from  random import randint
# candy = 2021
# player_1 = input('Введите имя игрока 1: ')
# player_2 = input('Введите имя игрока 2: ')
# list_choice = [player_1, player_2]
# random_choice = randint(0, len(list_choice)-1)

# print(f'Первым ходит игрок {list_choice[random_choice]}')
# print(f'{list_choice[random_choice]}, заберите не более 28 конфет у {list_choice[random_choice-1]}')
# turn_1 = input()








# Задача 107.
#---------------------------------------------------------------------------------
# Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)



# Задача 108.
#---------------------------------------------------------------------------------
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).