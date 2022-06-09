# Реализовать склонение слова «процент» во фразе "N процентов".
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 150.

# number = int(input('Please select an option: 1 - number or 2 - interval (enter 1 or 2): '))
# var_0 = 'процентов'
# var_1 = 'процент'
# var_2 = 'процента'
#
# if number == 1:
#     option_1 = input('Введите ваше число: ')
#     if int(option_1) // 10 > 0 or int(option_1) % 10 == 0:
#         if option_1[-2:] == '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19':
#             print(option_1, var_0)
#         elif option_1[-1] == '2' or '3' or '4':
#             print(option_1, var_2)
#     elif option_1[-1] == '1':
#         print(option_1, var_1)
#     else:
#         print(option_1, var_0)

# if number == 2:
#     option_2 = int(input('Введите интервал: '))
#     digit = 0
#     while digit < option_2:
#         digit += 1
#         if str(digit)[-1] == '0':
#             print(digit, var_0)
#         elif str(digit)[-2:] == '11' or '12' or '13' or '14' or '15' or '16' or '17' or '18' or '19':
#             print(digit, var_0)
#         elif str(digit)[-1] == '1':
#             print(digit, var_1)
#         elif str(digit)[-1] == '2' or '3' or '4':
#             print(digit, var_2)
#         else:
#             print(digit, var_0)

number = int(input('Please select an option: 1 - number or 2 - interval (enter 1 or 2): '))
var_0 = 'процентов'
var_1 = 'процент'
var_2 = 'процента'

if number == 1:
    option_1 = int(input('Enter your digit: '))
    if 20 > option_1 > 10 or option_1 % 100 == 1 and 20 > option_1 > 10 or option_1 % 10 == 0 or 20 > option_1 % 100 > 10:
        print(option_1, var_0)
    elif option_1 % 10 == 1 or (option_1 > 20 and option_1 % 10 == 1):
        print(option_1, var_1)
    elif 1 < option_1 < 5 and option_1 % 10 == option_1 or 5 > option_1 % 10 > 1:
        print(option_1, var_2)
    else:
        print(option_1, var_0)

if number == 2:
    option_2 = int(input('Enter your period: '))
    count = 0
    while count != option_2:
        count += 1
        if 20 > count > 10 or count % 100 == 1 and 20 > count > 10 or count % 10 == 0 or 20 > count % 100 > 10:
            print(count, var_0)
        elif count % 10 == 1 or (count > 20 and count % 10 == 1):
            print(count, var_1)
        elif 1 < count < 5 and count % 10 == count or 5 > count % 10 > 1:
            print(count, var_2)
        else:
            print(count, var_0)
