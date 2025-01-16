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

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание экземпляра магазина Sztum
sztum_store = Store("Sztum", "ул. Тараса Шевченко, 17")

# Добавляем товары в магазин
sztum_store.add_item("горные лыжи", 20000)
sztum_store.add_item("сноуборд", 15000)
sztum_store.add_item("горнолыжный костюм", 8000)

# Пример взаимодействия с пользователем через консоль
while True:
    print(f"\nДобро пожаловать в магазин {sztum_store.name}!")
    print(f"Наш адрес: {sztum_store.address}")
    print("\nМеню:")
    print("1. Узнать цену товара.")
    print("2. Выход.")

    choice = input("Введите номер пункта меню: ")

    if choice == "1":
        item_name = input("Введите название товара: ").lower()
        price = sztum_store.get_price(item_name)
        if price is not None:
            print(f"Цена товара '{item_name}' составляет {price} рублей.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")
    elif choice == "2":
        break
    else:
        print("Неверный ввод. Попробуйте снова.")

print("До свидания!")
