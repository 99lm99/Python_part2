from chess.queens import is_valid_queens, find_valid_queen_arrangements

# Пример проверки на бьющих друг друга ферзей
positions = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(f"Ферзи в позиции {positions} бьют друг друга: {not is_valid_queens(positions)}")

# Генерация случайных расстановок
successful_positions = find_valid_queen_arrangements()
for i, pos in enumerate(successful_positions):
    print(f"Успешная расстановка {i + 1}: {pos}")
