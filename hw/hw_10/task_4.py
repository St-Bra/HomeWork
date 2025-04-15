file_name = input("Enter file name: ")
import os
import re

def stop_words(file_name: str, stop_words_file_name):

    path = os.getcwd()
    file_path = os.path.join(path, file_name)

    with open(file_path, 'r') as f:
        file_text = f.read()
        file_text = file_text.lower()

    with open(stop_words_file_name, 'r') as f_1:
        stop_words_ = f_1.read().strip().split()

    for word in stop_words_:
        index = file_text.find(word)
        while index != -1:
            file_text = file_text[:index] + '*' * len(word) + file_text[index+len(word):]
            index = file_text.find(word, index + len(word))

    return file_text

print(stop_words(file_name, "stop_words.txt"))