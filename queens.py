"""3. Добавьте в пакет, созданный на семинаре шахматный модуль.Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""

import random

def is_valid_queens(positions):

    rows = set()
    cols = set()
    diag1 = set()  # x + y
    diag2 = set()  # x - y

    for x, y in positions:
        if x in rows or y in cols or (x + y) in diag1 or (x - y) in diag2:
            return False
        rows.add(x)
        cols.add(y)
        diag1.add(x + y)
        diag2.add(x - y)
    
    return True

def generate_random_positions():

    positions = []
    for i in range(1, 9):
        positions.append((i, random.randint(1, 8)))
    return positions

def find_valid_queen_arrangements(count=4):

    valid_arrangements = []
    attempts = 0

    while len(valid_arrangements) < count:
        attempts += 1
        positions = generate_random_positions()
        if is_valid_queens(positions):
            valid_arrangements.append(positions)

    print(f"Найдено {count} успешных расстановок после {attempts} попыток.")
    return valid_arrangements
