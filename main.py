#  Реализовать вывод информации о промежутке времени
#  в зависимости от его продолжительности duration в секундах.
# Формат вывода результата:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры/Тесты:
#
# duration = 53: 53 сек
# duration = 153: 2 мин 33 сек
# duration = 4153: 1 час 9 мин 13 сек
# duration = 400153: 4 дн 15 час 9 мин 13 сек

duration = int(input('Введите количество секунд: '))

if duration >= 86400:
    day = duration // 86400
    remain_day = duration % 86400
    hour = remain_day // 3600
    remain_hour = remain_day % 3600
    minutes = remain_hour // 60
    remain_minutes = remain_hour % 60
    print('duration =', str(duration) + ':', day, 'дн', hour, 'час', minutes, 'мин', remain_minutes, 'сек')
elif duration >= 3600:
    hour = duration // 3600
    remain_hour = duration % 3600
    minutes = remain_hour // 60
    remain_minutes = remain_hour % 60
    print('duration =', str(duration) + ':', hour, 'час', minutes, 'мин', remain_minutes, 'сек')
elif duration >= 60:
    second = duration // 60
    remain_second = duration % 60
    print('duration =', str(duration) + ':', second, 'мин', remain_second, 'сек')
else:
    print('duration =', str(duration) + ':', duration, 'сек')