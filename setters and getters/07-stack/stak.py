class TaskManager:
    def __init__(self):
        self.tasks = []  #стек задач в формате: (задача, приоритет)
    #метод добавляет новую задачу с указанным приоритетом
    def new_task(self, task, priority):
        self.tasks.append((task, priority))

    #метод возвращает строковое представление задач, отсортированных по приоритету
    def __str__(self):
        if not self.tasks:
            return "Нет задач"

        #сортируем задачи по приоритету
        sorted_tasks = sorted(self.tasks, key=self.get_priority)

        #формируем строку для вывода
        result = "\nОтсортированые по приоритету задачи:\n"
        for i, (task, priority) in enumerate(sorted_tasks, 1):
            result += f"{i}. {task} (приоритет: {priority})\n"

        return result
    #создаем функцию для сортировки
    def get_priority(self, task_item):
        return task_item[1]
    #метод удаляет последнюю добавленную задачу
    def remove_task(self):
        if self.tasks:
            return self.tasks.pop()
        return None
    #метод очищает все задачи
    def clear_all(self):
        self.tasks.clear()

#создаем экземпляр
manager = TaskManager()

#добавляем задачи с разными приоритетами
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("сдать дз", 2)
manager.new_task("поесть", 2)

#выводим отсортированные задачи
print(manager)

#добавляем еще одну задачу
manager.new_task("cходить за сигаретами", 1)
print("\nПосле добавления новой задачи:")
print(manager)

#удаляем последнюю задачу
removed = manager.remove_task()
print("\nПосле удаления задачи:")
print(manager)