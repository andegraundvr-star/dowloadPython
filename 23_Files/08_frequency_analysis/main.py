# Частотный анализ
#добавляем алфавит для подсчета латинских символов
alphabet_lower = [chr(i) for i in range(97, 123)]

#создаем функцию для подсчета частоты символов в строке
def sum_simbol_of_text(text):
    full_dict = {}
    total_simbols = 0

    #подсчитываем только буквы латинского алфавита
    for i_alp in text.lower():
        if i_alp in alphabet_lower:
            total_simbols += 1
            if i_alp in full_dict:
                full_dict[i_alp] += 1
            else:
                full_dict[i_alp] = 1

    #рассчитываем относительную частоту
    if total_simbols > 0:
        for i_len in full_dict:
            full_dict[i_len] = round(full_dict[i_len] / total_simbols, 3)

    return full_dict


#открываем файл
with open(r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\08_frequency_analysis\text.txt', 'r',
          encoding='utf-8') as file_text:
    #читаем весь текст из файла
    full_text = file_text.read()

    #применяем функцию подсчета частоты символов
    result = sum_simbol_of_text(full_text)

output_file = r'C:\Root\RemoteFolders\user0907\python-ds\23_Files\08_frequency_analysis\analysis.txt'
#функция перевода результатов в новый файл
def save_results(output_path, results):
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, (name, score) in enumerate(results.items(), 1):
            f.write(f" {name} {score}\n")
#сохраняем результаты
save_results(output_file, result)
