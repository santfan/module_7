# Импортируем небходимые библиотеки
import os
import time

# установим место старта сканирования в '.'
# Если установить старт '\\' - то сканироваться будет ВЕСЬ Диск С:
# В коде сформированном в Colab Google я ограничил диапазон сканирования
directory = '.'

# Пробежимся по дереву
for root, dirs, files in os.walk(directory):
    # теперь пробежимся по полученному результату итерации
    for file in files:
        # Получим путь к файлу относительно указанной директории поиска
        filepath = os.path.join(root,file)
        # Получим время изменения файла
        filetime = os.path.getmtime(filepath)
        # Отформатируем полученное время в удобочитаемый вид
        # (день, месяц, 4 цифры года и локальное время в виде час: минута)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        # Запроисм размер файла
        filesize = os.path.getsize(filepath)
        # Получим родительскую директорию
        parent_dir = os.path.dirname(filepath)

        # Выведем полученный результат итерации в данной директории
        print(f'Обнаружен файл: {file}')
        print(f'Путь: {filepath}')
        print(f'Время изменения: {formatted_time}, ')
        print(f'Размер: {filesize} байт, ')
        print(f'Родительская директория: {parent_dir}')
        print()