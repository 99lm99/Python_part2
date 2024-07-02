"""2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""



import os
import re

def batch_rename_files(desired_name, num_digits, old_extension, new_extension, name_range, directory='.'):
    # Список файлов для переименования
    files = [f for f in os.listdir(directory) if f.endswith(old_extension)]

    # Сортируем файлы для упорядоченного переименования
    files.sort()

    # Начинаем нумерацию с 1
    for idx, filename in enumerate(files, start=1):
        # Извлекаем часть имени файла по диапазону
        name_part = filename[name_range[0]-1:name_range[1]]

        # Формируем новый порядковый номер
        counter = str(idx).zfill(num_digits)

        # Формируем новое имя файла
        new_filename = f"{name_part}{desired_name}{counter}.{new_extension}"

        # Полные пути к файлам
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        print(f"'{filename}' -> '{new_filename}'")

# Пример использования
batch_rename_files(
    desired_name='_renamed',
    num_digits=3,
    old_extension='.txt',
    new_extension='txt',
    name_range=(3, 6),
    directory='/path/to/your/directory'  # Замените на ваш путь
)
