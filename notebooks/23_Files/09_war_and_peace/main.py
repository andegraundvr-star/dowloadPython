# Война и мир
import zipfile
import os

#добавляем алфавиты для подсчета латинских символов
alphabet_En = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
alphabet_Rus = [chr(i) for i in range(1040, 1104)]
#создаем функцию для сортировки
def sort_key(item):
    return (-item[1])

#создаем функцию для подсчета частоты символов в строке
def sum_simbol_of_text(text):
    full_dict = {}
    total_simbols = 0

    #подсчитываем буквы латинского и русского алфавитов
    for i_alp in text:
        if i_alp in alphabet_En:
            total_simbols += 1
            if i_alp in full_dict:
                full_dict[i_alp] += 1
            else:
                full_dict[i_alp] = 1
        elif i_alp in alphabet_Rus:
            total_simbols += 1
            if i_alp in full_dict:
                full_dict[i_alp] += 1
            else:
                full_dict[i_alp] = 1
    return full_dict

#открываем файл
zip_path = r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\09_war_and_peace\voyna-i-mir.zip'
extract_dir = r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\09_war_and_peace'  #распаковываем в директорию
#распаковываем весь архив
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    #получаем список файлов в архиве
    file_list = zip_ref.namelist()
    if not file_list:
        print("Архив пуст!")
        exit()
#распаковываем первый файл из архива
    text_file_name = file_list[0]
    zip_ref.extract(text_file_name, extract_dir)
    print(f"Файл {text_file_name} распакован в: {extract_dir}")


file_path = os.path.join(extract_dir, text_file_name)#джойним путь к файлу и название
#читаем распакованный файл
with open(file_path, 'r', encoding='utf-8') as file:
    full_text = file.read()
    #применяем функцию подсчета частоты символов
    result = sum_simbol_of_text(full_text)

    #сортируем с помощью функции сортировки
    sorted_result = sorted(result.items(), key=sort_key)

    #выводим результаты
    print("Полная статистика по строчным и заглавным символам (отсортировано по частоте):")
    for simbol, freq in sorted_result:
        print(f"{simbol}: {freq}")


