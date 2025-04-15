from db import (init_db, add_course, add_teacher, add_student, enroll_student, get_student_progress,
                              search_course_by_name, del_course, get_all_courses, del_teacher, del_student,
                              edit_course, edit_teacher, edit_student, get_all_teachers, get_all_students)

def print_menu():
    """Выводит меню команд"""
    print("\nВыберите действие:")
    print("0. Выход")
    print("1. Действия с курсом")
    print("2. Действия с преподавателем")
    print("3. Действия с студентом")
    print("4. Поставить оценку студенту")
    print("5. Посмотреть прогресс студента")
    print("6. Найти курс по названию")

def main():
    """Основная логика программы"""
    init_db()  # Создание таблиц при запуске
    print("Добро пожаловать в IT онлайн школу!")

    while True:
        print_menu()
        choice = input("Введите номер действия: ").strip()

        if choice == "0":
            print("👋 До свидания!")
            break

        elif choice == "1":
            print("\nВыберите действие:")
            print("0. Выход")
            print("1. Добавить курс")
            print("2. Удалить курс")
            print("3. Редактировать курс")
            print("4. Посмотреть список курсов")

            choice = input("Введите номер действия: ").strip()

            if choice == "0":
                continue
            elif choice == "1":
                name = input("Название курса: ").strip()
                description = input("Описание курса: ").strip()
                try:
                    course_id = add_course(name, description)
                    print(f"✅ Курс добавлен (ID: {course_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "2":
                course_id = input("Введите ID курса для удаления: ").strip()
                try:
                    del_course(course_id)
                    print(f"✅ Курс удалён (ID: {course_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "3":
                course_id = input("Введите ID курса для редактирования: ").strip()
                new_name = input("Новое название курса: ").strip()
                new_description = input("Новое описание курса: ").strip()
                try:
                    edit_course(course_id, new_name, new_description)
                    print(f"✅ Курс отредактирован (ID: {course_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "4":
                courses = get_all_courses()
                if courses:
                    print("\n📚 Список всех курсов:")
                    for course in courses:
                        print(f"🔹 ID: {course[0]}, Название: {course[1]}, Описание: {course[2]}")
                else:
                    print("ℹ Нет курсов.")

        elif choice == "2":
            print("\nВыберите действие:")
            print("0. Выход")
            print("1. Добавить преподавателя")
            print("2. Удалить преподавателя")
            print("3. Редактировать преподавателя")
            print("4. Посмотреть список преподавателей")

            choice = input("Введите номер действия: ").strip()

            if choice == "0":
                continue
            elif choice == "1":
                name = input("Имя преподавателя: ").strip()
                email = input("Email преподавателя: ").strip()
                try:
                    teacher_id = add_teacher(name, email)
                    print(f"✅ Преподаватель добавлен (ID: {teacher_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "2":
                teacher_id = input("Введите ID преподавателя для удаления: ").strip()
                try:
                    del_teacher(teacher_id)
                    print(f"✅ Преподаватель удалён (ID: {teacher_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "3":
                teacher_id = input("Введите ID преподавателя для редактирования: ").strip()
                new_name = input("Новое имя преподавателя: ").strip()
                new_email = input("Новый email преподавателя: ").strip()
                try:
                    edit_teacher(teacher_id, new_name, new_email)
                    print(f"✅ Преподаватель отредактирован (ID: {teacher_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "4":
                teachers = get_all_teachers()
                if teachers:
                    print("\n👨‍🏫 Список всех преподавателей:")
                    for teacher in teachers:
                        print(f"🔹 ID: {teacher[0]}, Имя: {teacher[1]}, Email: {teacher[2]}")
                else:
                    print("ℹ Нет преподавателей.")

        elif choice == "3":
            print("\nВыберите действие:")
            print("0. Выход")
            print("1. Добавить студента")
            print("2. Удалить студента")
            print("3. Редактировать студента")
            print("4. Посмотреть список студентов")

            choice = input("Введите номер действия: ").strip()

            if choice == "0":
                continue
            elif choice == "1":
                name = input("Имя студента: ").strip()
                email = input("Email студента: ").strip()
                try:
                    student_id = add_student(name, email)
                    print(f"✅ Студент добавлен (ID: {student_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "2":
                student_id = input("Введите ID студента для удаления: ").strip()
                try:
                    del_student(student_id)
                    print(f"✅ Студент удалён (ID: {student_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "3":
                student_id = input("Введите ID студента для редактирования: ").strip()
                new_name = input("Новое имя студента: ").strip()
                new_email = input("Новый email студента: ").strip()
                try:
                    edit_student(student_id, new_name, new_email)
                    print(f"✅ Студент отредактирован (ID: {student_id})")
                except Exception as e:
                    print(f"⚠ Ошибка: {e}")
            elif choice == "4":
                students = get_all_students()
                if students:
                    print("\n👩‍🎓 Список всех студентов:")
                    for student in students:
                        print(f"🔹 ID: {student[0]}, Имя: {student[1]}, Email: {student[2]}")
                else:
                    print("ℹ Нет студентов.")

        elif choice == "4":
            try:
                student_id = int(input("ID студента: ").strip())
                course_id = int(input("ID курса: ").strip())
                grade = input("Оценка (если есть, иначе Enter): ").strip()
                grade = int(grade) if grade else None
                enroll_student(student_id, course_id, grade)
                print("✅ Студент получил оценку!")
            except ValueError:
                print("⚠ Ошибка: ID и оценка должны быть числами.")
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

        elif choice == "5":
            try:
                student_id = int(input("ID студента: ").strip())
                progress = get_student_progress(student_id)
                if progress:
                    print("\n📊 Прогресс студента:")
                    for course, grade in progress:
                        grade_text = grade if grade is not None else "Нет оценки"
                        print(f"📌 Курс: {course}, Оценка: {grade_text}")
                else:
                    print("ℹ Студент ещё не записан на курсы.")
            except ValueError:
                print("⚠ Ошибка: ID должен быть числом.")
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

        elif choice == "6":
            name = input("Введите часть названия курса: ").strip()
            try:
                courses = search_course_by_name(name)
                if courses:
                    print("\n📚 Найденные курсы:")
                    for course in courses:
                        print(f"🔹 ID: {course[0]}, Название: {course[1]}, Описание: {course[2]}")
                else:
                    print("ℹ Курсы не найдены.")
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

        else:
            print("⚠ Ошибка: Неверный ввод. Попробуйте снова.")

main()
