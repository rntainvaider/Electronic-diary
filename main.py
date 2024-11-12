from os import name
import random

import comm

# список учеников
students = ["Аполлон", "Ярослав", "Александра", "Дарья", "Ангелина"]
# отсортируем список учеников
students.sort()
# список предметов
classes = ["Математика", "Русский язык", "Информатика"]
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [
            random.randint(1, 5) for _ in range(3)
        ]  # генерируем список из 3х случайных оценок
        students_marks[student][
            class_
        ] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f"""{student} {students_marks[student]}""")


print(
    """
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Вывести все оценки по одному ученику
5. Удалить ученика
6. Изменить оценки ученика
0. Выход из программы
"""
)

while True:
    command = int(input("Введите команду: "))
    if command == 1:
        print("1. Добавить оценку ученика по предмету")
        # считываем имя ученика
        student = input("Введите имя ученика: ")
        # считываем название предмета
        class_ = input("Введите предмет: ")
        # считываем оценку
        mark = int(input("Введите оценку: "))
        # если данные введены верно
        if (
            student in students_marks.keys()
            and class_ in students_marks[student].keys()
        ):
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f"Для {student} по предмету {class_} добавлена оценка {mark}")
        # неверно введены название предмета или имя ученика
        else:
            print("ОШИБКА: неверное имя ученика или название предмета")
    elif command == 2:
        print("2. Вывести средний балл по всем предметам по каждому ученику")
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f"{class_} - {marks_sum//marks_count}")
            print()
    elif command == 3:
        print("3. Вывести все оценки по всем ученикам")
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f"\t{class_} - {students_marks[student][class_]}")
            print()
    elif command == 4:
        print("4. Вывести все оценки по одному ученику")
        name_student = input("Введите имя ученика: ")
        if name_student in students_marks.keys():
            print(f"""{name_student} - {students_marks[name_student]}""")
        else:
            print("ОШИБКА: неверное имя ученика")
    elif command == 5:
        print("5. Удалить ученика")
        name_student = input("Введите имя ученика: ")
        if name_student in students:
            students.remove(name_student)
            print(f"Ученик {name_student} был удалён")
        else:
            print("ОШИБКА: неверное имя ученика")
    elif command == 6:
        print("6. Изменить оценки ученика")
        name = input("Введите имя ученика: ")
        class_ = input("Введите предмет: ")
        if name in students_marks.keys() and class_ in students_marks[name].keys():
            numb_mark = int(input("Введите номер оценки которую хотите изменить: "))
            mark = int(input("Введите оценку на которую хотите заменить: "))
            for item in students_marks[name][class_]:
                if students_marks[name][class_][numb_mark - 1] == item:
                    students_marks[name][class_][numb_mark - 1] = mark
                print("Такого номера оценки нет!")
            print("Оценка изменена!")
        else:
            print("Такого ученика не существует или название предмета")
    elif command == 0:
        print("0. Выход из программы")
        break
