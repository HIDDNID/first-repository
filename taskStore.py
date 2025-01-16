class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

# Пример использования
store = Store('Sklad', 'Щелковское шоссе, 40')

# Добавляем товары
store.add_item('Белая кофта', 1500)
store.add_item('Синие джинсы', 2500)
store.add_item('Черные ботинки', 3000)

# Получение цены товара
price = store.get_price('Белая кофта')
print(f"Цена белой кофты: {price}")

# Обновление цены товара
store.update_price('Синие джинсы', 2700)
new_price = store.get_price('Синие джинсы')
print(f"Новая цена синих джинсов: {new_price}")

# Удаление товара
store.remove_item('Черные ботинки')
