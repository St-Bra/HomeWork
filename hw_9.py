import os
import re

# Задание 1

# Получаем имя ОС
os_name = os.name
print(f"Имя вашей ОС: {os_name}")

# Получаем текущий путь
current_path = os.getcwd()
print(f"Путь до текущей папки: {current_path}")

# Создаем словарь для хранения информации о перемещенных файлах
files_info = {}

# Проходим по файлам в текущей директории
for file in os.listdir(current_path):
    file_path = os.path.join(current_path, file)
    if os.path.isfile(file):
        file_ext = os.path.splitext(file)[1]  # Получаем расширение файла

        if file_ext:  # Пропускаем файлы без расширения
            folder_name = file_ext[1:]  # Убираем точку из расширения
            folder_path = os.path.join(current_path, folder_name)

            # Создаем папку, если её нет
            os.makedirs(folder_path, exist_ok=True)

            # Перемещаем файл в папку
            new_file_path = os.path.join(folder_path, file)
            os.rename(file_path, new_file_path)

            # Обновляем информацию о перемещенных файлах
            file_size = os.path.getsize(new_file_path)
            if folder_name not in files_info:
                files_info[folder_name] = {'count': 0, 'size': 0}
            files_info[folder_name]['count'] += 1
            files_info[folder_name]['size'] += file_size

# Вывод информации о перемещенных файлах
for ext, info in files_info.items():
    print(f"В папке с файлами .{ext} перемещено {info['count']} файлов, их суммарный размер - {info['size']} байт.")

# Переименование одного файла в каждой папке
for ext in files_info.keys():
    folder_path = os.path.join(current_path, ext)
    files = os.listdir(folder_path)

    if files:
        old_file_name = files[0]
        old_file_path = os.path.join(folder_path, old_file_name)

        new_file_name = f"some_{old_file_name}"
        new_file_path = os.path.join(folder_path, new_file_name)

        os.rename(old_file_path, new_file_path)
        print(f"Файл {old_file_name} был переименован в {new_file_name}")

#Задание 2

text = """Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии алкогольного опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного телефона в полицию, сообщив о том, что у неё в квартире якобы заложена бомба. После чего приехали сотрудники полиции, скорая и пожарные, которым она сообщила, что бомба — это она."""

pattern = r"(Подсудимая\s+[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+)"

modified_text = re.sub(pattern, "Подсудимая N", text)

print(modified_text)