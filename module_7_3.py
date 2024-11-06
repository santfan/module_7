# Объявим класс WordFinder
class WordFinder:
  '''Класс принимает неограниченное колличество файлов
  В качестве аргументов принимаются файлы.
  Обращение к аргументам осуществляется по именам'''

# Функция инициации
  def __init__(self, *file_names):
    self.file_names = file_names

# Функция формирования списка слов в файле
  def get_all_words(self):
    # Установим словарь слов файла в нулевое значение
    all_words = {}
    # Для каждого файла
    for file_name in self.file_names:
      # Откроем файл как file
      with open(file_name, 'r', encoding='utf-8') as file:
        # Прочитаем файл и приведем все слова к нижнему регистру
        words = file.read().lower()
        # Сформируем словарь с ключом название файла и исключим знаки пунктуации
        if words not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
          all_words[file_name] = words.split()
    # Вернем словарь слов
    return all_words

# Функция поиска позиции слова
  def find(self, word):
    # Приведем слово к нижнему регистру
    word = word.lower()
    # Позицию искомого слова установим в пустое значение
    word_pos = {}

    # Отберем в словаре патерны ключ-значения
    for file_name, words in self.get_all_words().items():
      # Если искомое слово в списке слов
      if word in words:
        # Установим значение индекса
        word_pos[file_name] = words.index(word) + 1

    # Вернем значение позиции
    return word_pos

# Функция подсчета вхождений слова
  def count(self, word):
    # Приведем слово к нижнему регистру
    word = word.lower()
    # Счетчик вхождения в пустое значени
    word_count ={}
    # Пробежим по словарю и отберем пары ключ-значение
    for file_name, words in self.get_all_words().items():
      # Если слово в списке слов
      if word in words:
        # Посчитаем количество вхождений
        word_count[file_name] = words.count(word)

    return word_count


# Проверка на тестовом файле
finder2 = WordFinder('test_file.txt')

print(finder2.get_all_words())

print(finder2.find('Text'))

print(finder2.count('TeXt'))

# Проверка на файле Mother Goose - Monday’s Child
finder1 = WordFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

# Проверка на файле Rudyard Kipling - If
finder3 = WordFinder('Rudyard Kipling - If.txt',)
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))

# Проверка на файле Walt Whitman - O Captain! My Captain!
finder4 = WordFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder4.get_all_words())
print(finder4.find('captain'))
print(finder4.count('captain'))

# Проверка на группе файлов
finder5 = WordFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder5.get_all_words())
print(finder5.find('the'))
print(finder5.count('the'))

