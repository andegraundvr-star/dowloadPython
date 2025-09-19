#Студент
#создаем класс
class Student:
    def __init__(self, name):
        self.name = name
        self.group_nomber = ''
        self.marks = []
    #добавление оценок в список и проверка перед вводом
    def add_marks(self,marks_input):
        try:
            marks_list = marks_input.split()
            #проверяем, что все оценки - цифры от 1 до 9
            if all(mark.isdigit() and len(mark) == 1 and 1 <= int(mark) <= 9 for mark in marks_list):
                self.marks.extend([int(mark) for mark in marks_list])
                return True
            else:
                print("Ошибка: оценки должны быть цифрами от 1 до 9 через пробел")
                return False
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
            return False

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
#класс группы
class Group:
    def __init__(self,group_nomber):
        self.group_nomber = group_nomber
        self.list_students = []

    #добавляем студента в группу
    def add_student(self, student):
        student.group_nomber = self.group_nomber
        self.list_students.append(student)
    #добавляем метод для ввода студентов и их оценок
    def input_students(self):
        while True:
            name = input("\nВведите имя и фамилию студента (или 'стоп' для завершения): ")
            if name.lower() == 'стоп':
                break
            if len(name.split()) < 2:
                print("Ошибка: введите имя и фамилию через пробел")
                continue
            student = Student(name)
            #ввод оценок с проверкой
            while True:
                marks_input = input(f"Введите оценки студента {name} через пробел: ")
                if student.add_marks(marks_input):
                    break  #выход из цикла, если оценки введены корректно
            self.add_student(student)
            print(f"Студент {name} добавлен в группу {self.group_nomber}")

    #cоздаем сортированный список
    def get_top_students(self, top_n=10):
        student_avg_marks = []
        for student in self.list_students:
            avg = student.average_mark()
            student_avg_marks.append((avg, student.name))
        #сортируем по убыванию среднего балла
        student_avg_marks.sort(reverse=True)
        #выводим топ-N студентов
        print(f"\nТоп-{top_n} студентов группы {self.group_nomber}:")
        for i, (avg, name) in enumerate(student_avg_marks[:top_n], 1):
            print(f"{i}. {name}: {avg:.2f}")
#запуск модели
#cоздаем группу
group = Group("ГР-01")

group.input_students()
group.get_top_students()



