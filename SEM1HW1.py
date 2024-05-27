# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
#
# a = 3
# b = 3
# c = 3
#
# if a + b < c or a + c < b or b + c < a:
#     print('no appear')
# elif (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
#     print('ravnobedren')
# elif a != b and b != c and c != a:
#     print('raznostor')
# elif a == b and b == c and a == c:
#     print('ravnostoron')


# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

#
# LIMIT_MIN = 0
# LIMIT_MAX = 100000
#
# num = LIMIT_MIN
#
# num = int(input(f'add number from {LIMIT_MIN} to {LIMIT_MAX}: '))
# if num > LIMIT_MIN and num < LIMIT_MAX:
#     if num % num == 0 and num % 1 == 0 and num % 2 != 0 and num % 3 != 0:
#         print(f'{num} is prostoe')
#     else:
#         print(f'{num} is sostavnoe')
# else:
#     num = int(input(f'add number from {LIMIT_MIN} to {LIMIT_MAX}: '))


# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print(f'guess digit from {LOWER_LIMIT} to {UPPER_LIMIT}')
print(num)
for i in range(1,MAX_COUNT + 1):
    guest = int(input(f'Chance №' + str(i) + ': '))
    if guest < num:
        print('Sorry, your digit is low')
    elif guest > num:
        print('Sorry, your digit is upper')
    else:
        print('Congratulations you guess!')
        break
else:
    print('Sorry you dont guess')
