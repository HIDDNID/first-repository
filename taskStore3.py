class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет новый товар в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name)

    def update_price(self, item_name, discount_percentage):
        """
        Обновляет цену товара с учетом скидки.
        :param item_name: Название товара.
        :param discount_percentage: Процент скидки в десятичной форме (например, 0.15 означает 15%).
        """
        if item_name in self.items:
            current_price = self.items[item_name]
            discounted_price = current_price * (1 - discount_percentage)
            self.items[item_name] = round(discounted_price, 2)

    def check_availability(self, item_name):
        """Проверяет доступность товара."""
        return item_name in self.items


# Создание экземпляра магазина Cifry
cifry_store = Store("Cifry", "Ленинский проспект, 99")

# Добавляем товары в магазин
cifry_store.add_item("ноутбук", 70000)
cifry_store.add_item("телефон", 30000)
cifry_store.add_item("планшет", 25000)

# Убираем все телефоны из продажи
cifry_store.remove_item("телефон")

# Применяем скидку 15% на оставшиеся товары
for item in cifry_store.items.keys():
    cifry_store.update_price(item, 0.15)

# Пример взаимодействия с пользователем через консоль
while True:
    print(f"\nДобро пожаловать в магазин {cifry_store.name}!")
    print(f"Наш адрес: {cifry_store.address}")
    print("\nМеню:")
    print("1. Запросить информацию о товаре.")
    print("2. Выход.")

    choice = input("Введите номер пункта меню: ")

    if choice == "1":
        item_name = input("Введите название товара: ").lower()

        # Проверка наличия товара
        if cifry_store.check_availability(item_name):
            price = cifry_store.get_price(item_name)
            print(f"{item_name.capitalize()} сейчас стоит {price} рублей. Цена изменилась по акции!")
        else:
            print(f"К сожалению, {item_name} уже распродан.")

    elif choice == "2":
        break
    else:
        print("Неверный ввод. Попробуйте снова.")

print("До свидания!")
