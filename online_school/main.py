import db

def print_menu():
    print("Выберите нужную команду:")
    print("0. Выход")
    print("1. Показать список курсов")
    print("2. Показать список студентов")
    print("3. Показать список преподавателей")
    print("4. Показать информацию об успеваемости студента по id")
    print("5. Добавить студента")
    print("6. Поиск студента по имени")

def app():
    db.init_db()
    print('Таблицы успешно созданы')
 
    # print("Вас приветствует, IT онлайн школа!")
    # while True:
    #     print_menu()
    #     cmd = int(input("Введите номер команды: "))

    #     if cmd == 0:
    #         print("До скорой встречи!)")
    #         break
    #     elif cmd == 1:
    #         pass
    #     elif cmd == 2:
    #         pass
    #     elif cmd == 3:
    #         pass
    #     elif cmd == 4:
    #         pass
    #     elif cmd == 5:
    #        pass
    #     elif cmd == 6:
    #         pass
    #     else:
    #         print("Вы ввели несуществующею команду. Попробуйте еще раз!")

app()