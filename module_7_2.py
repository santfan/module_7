# Создадим функцию
def custom_file(file_name, strings):
    # Создадим пустой словарь
    result_dict = {}
    # Взведем счетчик строк
    num = 0
    # Откроем переданный файл поддержкой кириллицы
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        num += 1
        # Определим положение курсора
        cursor = file.tell()
        # Заполним словарь
        result_dict[(num, cursor)] = string
        # Запишем значение в файл
        file.write(string + '\n')
    # Закроем открытый файл
    file.close()
    # Вернем сформированный словарь
    return result_dict

# Файл с коллекцией строковых значений
info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']
# Вызовем функцию и распечатаем словарь
for elem in custom_file('test.txt', info).items():
    print(elem)

