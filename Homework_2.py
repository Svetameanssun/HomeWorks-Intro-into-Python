# Домашнее задание Семинар 2

#---------------------------------------------------------------------------------
# Задача 10
#---------------------------------------------------------------------------------
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
# import random
# coins = []
# n = 10
# for i in range(n):
#     coins.append(random.randint(0,1))
# print(coins)
# sum_tails = 0
# sum_heads = 0
# for i in range(n):
#     if coins[i] == 0:
#         sum_tails +=1
#         i+=1
#     elif coins[i] == 1:
#         sum_heads +=1
#         i+=1
# if sum_tails > sum_heads:
#     print(f'нужно перевернуть {sum_heads} монет(ы).')
# else:
#     print(f'нужно перевернуть {sum_tails} монет(ы).')


#---------------------------------------------------------------------------------
# Задача 12
#---------------------------------------------------------------------------------
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает
# два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# import random
# number1 = int(random.uniform(0,11))
# number2 = int(random.uniform(0,11))
# print(number1, number2)
# number1 + number2 = sum
# number1 * number2 = product
summ_xy = int(input('summ = '))
product_xy = int(input('product = '))
a = 1 # всегда получается такое уравнение: y**2 - sum*y + pr = 0, поэтому а всегда равно 0
discriminant = (-summ_xy)**2 - (4*a*product_xy)
print('Discriminant: '+str(discriminant))
if discriminant < 0:
    print('There is no square root from discriminant!')
elif discriminant == 0:
    x = -(-summ_xy) / (2*a)
    if x%1 != 0:
        print("X and y are not natural numbers!")
    else:
        print(f'The both numbers equal {x}')
else:
    x = (-(-summ_xy) + discriminant**0.5)/ 2*a
    y = (-(-summ_xy) - discriminant**0.5)/ 2*a
    if x%1 != 0 and y%1 != 0:
        print(f'{x} and {y} are not natural numbers!')
    else:
        print(f'One number equals {x}, the other equals {y}')




#---------------------------------------------------------------------------------
# Задача 14
#---------------------------------------------------------------------------------
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# power = 0
# power_result = 1
# N = 1024
# list = []
# while power_result <= N - (2**(power-1)):
#     power_result = 2**power
#     list.append(power_result)
#     power +=1
# print(list)

