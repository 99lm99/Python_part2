# Урок 4. Функции
# Условие
# 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])  
    

    transposed = [[0] * rows for _ in range(cols)]
    

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Транспонированная матрица:")
transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)





# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hasattr(value, '__hash__'):
            result[value] = key
        else:
            result[str(value)] = key
    return result

# Пример использования функции
dict1 = create_dict(a=10, b='hello', c=[1, 2, 3])
dict2 = create_dict(x=100, y=(1, 2, 3), z=100)

print("Словарь 1:")
print(dict1)

print("\nСловарь 2:")
print(dict2)
