class Task:
    def __init__(self, description, due_date, status=False):
        """
        Конструктор класса Task.

        :param description: Описание задачи
        :param due_date: Срок выполнения задачи
        :param status: Статус задачи (True - выполнена, False - не выполнена)
        """
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_as_done(self):
        """Отметить задачу как выполненную."""
        self.status = True

    def is_completed(self):
        """Проверяет, завершена ли задача."""
        return self.status

    def __repr__(self):
        """Представление задачи в виде строки."""
        status_str = "Выполнена" if self.status else "Не выполнена"
        return f"{self.description} (срок: {self.due_date}, статус: {status_str})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Добавляет новую задачу в список задач."""
        self.tasks.append(task)

    def complete_task(self, index):
        """Изменяет статус задачи на выполненную."""
        try:
            self.tasks[index].mark_as_done()
        except IndexError:
            print(f"Задача с индексом {index} не найдена.")

    def get_all_tasks(self):
        """Возвращает список всех задач."""
        return self.tasks

    def display_all_tasks(self):
        """Выводит список всех задач."""
        tasks = self.get_all_tasks()
        if len(tasks) == 0:
            print("Нет задач.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    def get_incomplete_tasks(self):
        """Возвращает список всех невыполненных задач."""
        incomplete_tasks = [task for task in self.tasks if not task.is_completed()]
        return incomplete_tasks

    def display_incomplete_tasks(self):
        """Выводит список всех невыполненных задач."""
        tasks = self.get_incomplete_tasks()
        if len(tasks) == 0:
            print("Нет невыполненных задач.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.description} (до {task.due_date})")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    # Добавление нескольких задач
    manager.add_task(Task("Сделать домашнюю работу", "01-01-2025"))
    manager.add_task(Task("Купить продукты", "02-10-2025"))
    manager.add_task(Task("Позвонить бабушке", "03-10-2025"))

    # Отмечаем первую задачу как выполненную
    manager.complete_task(0)

    # Выводим список всех задач
    manager.display_all_tasks()

    # Выводим список невыполненных задач
    manager.display_incomplete_tasks()
