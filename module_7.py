# Объявим класс Product
class Product:
    '''Класс Product принимает атрибуты:
        name (имя товара) - тип str
        weight (вес товара) - тип float
        category (Категория товара) - тип str'''

    # Функция инициации
    def __init__(self, name: str, weight: float, category: str ):
        self.name = name
        self.weight = weight
        self.category = category

    # Функция переопределения вывода строкового типа
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

# Объявим класс Shop
class Shop():
    '''Класс Shop имеет:
        Инкапсулированный атрибут __file_name
        Метод get_products считывает данные из файла __file_name
        Метод add принимает новые товары, проверяет есть ли аналогичная запись,
        усли такой записи нет эта запись добавляется'''

    __file_name = 'products.txt'

    # Метод считывания данных
    def get_products(self):
        # откроем файл для четния
        file = open(self.__file_name, 'r')
        # Прочитаем файл
        products = file.read()
        # Закроем открытый файл
        file.close()
        # Вернем считанный файл
        return products

    # Метод add (добавление товара)
    def add(self, *products):
        # волучим сведения о внесенных в файл товаров
        current_products = self.get_products()
        # Откроем файл для записи
        file = open(self.__file_name, 'a')
        # Проверим есть ли запись для товара в файле
        for product in products:
            if str(product) not in current_products:
                file.write(str(product) + '\n')
                current_products += str(product) + '\n'
            # Если запись уже есть
            else:
                print(f'Товар {product} уже внесен в файл')
        # Закроем открытый файл
        file.close()

# создадим экземпляр Shop
s1 = Shop()
# Три экзмпляра товаров
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Проверим результат создания товаров
print(p1)
print(p2)
print(p3)

# Добавим эти товары в список и проверим результат
s1.add(p1, p2, p3)
print(s1.get_products())

s1.add(p1, p2, p3)
# Посмотрим содержимое файл products
print(s1.get_products())


