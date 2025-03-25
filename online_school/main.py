from db import init_db, add_course, add_teacher, add_student, enroll_student, get_student_progress, search_course_by_name

def print_menu():
    """Выводит меню команд"""
    print("\nВыберите действие:")
    print("1. Добавить курс")
    print("2. Добавить преподавателя")
    print("3. Добавить студента")
    print("4. Записать студента на курс")
    print("5. Посмотреть прогресс студента")
    print("6. Найти курс по названию")
    print("7. Выход")

def main():
    """Основная логика программы"""
    init_db()  # Создание таблиц при запуске
    print("Добро пожаловать в IT онлайн школу!")

    while True:
        print_menu()
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            name = input("Название курса: ").strip()
            description = input("Описание курса: ").strip()
            try:
                course_id = add_course(name, description)
                print(f"✅ Курс добавлен (ID: {course_id})")
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

        elif choice == "2":
            name = input("Имя преподавателя: ").strip()
            email = input("Email преподавателя: ").strip()
            try:
                teacher_id = add_teacher(name, email)
                print(f"✅ Преподаватель добавлен (ID: {teacher_id})")
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

        elif choice == "3":
            name = input("Имя студента: ").strip()
            email = input("Email студента: ").strip()
            try:
                student_id = add_student(name, email)
                print(f"✅ Студент добавлен (ID: {student_id})")
            except Exception as e:
                print(f"⚠ Ошибка: {e}")

        elif choice == "4":
            try:
                student_id = int(input("ID студента: ").strip())
                course_id = int(input("ID курса: ").strip())
                grade = input("Оценка (если есть, иначе Enter): ").strip()
                grade = int(grade) if grade else None
                enroll_student(student_id, course_id, grade)
                print("✅ Студент записан на курс!")
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

        elif choice == "7":
            print("👋 До свидания!")
            break

        else:
            print("⚠ Ошибка: Неверный ввод. Попробуйте снова.")


main()