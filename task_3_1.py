# Реализовать склонение слова «процент» во фразе "N процентов".
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 150.
# Формат вывода результата:
# 0 процентов
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# и т.п.
#
# Алгоритм:
# Ваш алгоритм должен корректно работать и для интервала от 1 до 150,
# и для любого числа(заведенного в код), например от 1 до 1000.
# Правила склонения здесь достаточно просты: всего три варианта:
# «процент»/«процента»/«процентов».
# Обратите внимание на диапазон 10-19 и как он повторяется.

# number = int(input('Please select an option: 1 - number or 2 - interval (enter 1 or 2): '))
# var_0 = 'процентов'
# var_1 = 'процент'
# var_2 = 'процента'

# if number == 1:
#     option_1 = input('Введите ваше число: ')
#     if option_1[-1] == '1':
#         print(option_1, var_1)
#     if option_1[-1] == '0':
#         print(option_1, var_0)
#     if option_1[-2:] == '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19':
#         print(option_1, var_0)
#     if option_1[-1] == '2' or '3' or '4':
#         print(option_1, var_2)
#     # else:
#     #     print(option_1, var_0)

# if number == 2:
#     option_2 = int(input('Введите интервал: '))
#     digit = 0
#     while digit < option_2:
#         digit += 1
#         if str(digit)[-1] == '0':
#             print(digit, var_0)
#         elif str(digit)[:-2] == '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19':
#             print(digit, var_0)
#         elif str(digit)[-1] == '1':
#             print(digit, var_1)
#         elif str(digit)[-1] == '2' or '3' or '4':
#             print(digit, var_2)
#         else:
#             print(digit, var_0)

a = 'asd'
c = input()
sb = b'a'
ds = b'c'
print(c)
print(c[0])
print(ds[0])
print(a)
print(a[0])
print(sb[0])
