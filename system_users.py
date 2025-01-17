class User:
    def __init__(self, user_id, name, access_level="user"):
        self._id = user_id
        self._name = name
        self._access_level = access_level

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name

    def set_access_level(self, new_access_level):
        self._access_level = new_access_level

    def __repr__(self):
        return f"User({self.get_id()}, '{self.get_name()}', '{self.get_access_level()}')"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level="admin")
        self._users = []
        self._added_by = {}
        self._deleted_by = {}

    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Argument must be a User object.")
        self._users.append(user)
        self._added_by[user.get_id()] = self.get_name()

    def remove_user(self, user_id):
        for index, user in enumerate(self._users):
            if user.get_id() == user_id:
                self._deleted_by[user_id] = self.get_name()
                del self._users[index]
                return True
        return False

    def list_users(self):
        return self._users

    def who_added(self, user_id):
        return self._added_by.get(user_id, None)

    def who_deleted(self, user_id):
        return self._deleted_by.get(user_id, None)

    def __repr__(self):
        return f"Admin({self.get_id()}, '{self.get_name()}', '{self.get_access_level()}')"


# Создаем администраторов
roman_sh = Admin(101, "Роман Ш.")
inna_d = Admin(102, "Инна Д.")

# Создаем обычных пользователей
natalia_g = User(201, "Наталья Г.", "user")
oleg_l = User(202, "Олег Л.", "user")
vladimir_o = User(203, "Владимир О.", "user")
gennadiy_i = User(204, "Геннадий И.", "user")
lilia_s = User(205, "Лилия С.", "user")

# Добавляем пользователей под управление Роману Ш.
roman_sh.add_user(natalia_g)
roman_sh.add_user(oleg_l)
roman_sh.add_user(vladimir_o)
roman_sh.add_user(gennadiy_i)
roman_sh.add_user(lilia_s)

# Список пользователей под управлением Романа Ш.
print("Пользователи под управлением Романа Ш.:")
for user in roman_sh.list_users():
    print(user)

# Удаляем Геннадия И. из системы
removed = roman_sh.remove_user(204)
if removed:
    print("\nГеннадий И. был успешно удален.")
    print(f"Удалил: {roman_sh.who_deleted(204)}")
else:
    print("\nНе удалось удалить Геннадия И.")

# Обновленный список пользователей под управлением Романа Ш.
print("\nОбновленный список пользователей:")
for user in roman_sh.list_users():
    print(user)

# Инна Д. добавляет трех новых пользователей
irina_k = User(206, "Ирина К.", "user")
sergey_m = User(207, "Сергей М.", "user")
olga_p = User(208, "Ольга П.", "user")

inna_d.add_user(irina_k)
inna_d.add_user(sergey_m)
inna_d.add_user(olga_p)

# Список пользователей под управлением Инны Д.
print("\nПользователи под управлением Инны Д.:")
for user in inna_d.list_users():
    print(user)

# Отслеживаем, кто добавил новых пользователей
print("\nИнформация о добавленных пользователях:")
for user_id in inna_d._added_by.keys():
    print(f"Пользователь с ID {user_id} был добавлен {inna_d._added_by[user_id]}.")
