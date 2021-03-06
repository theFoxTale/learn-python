"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    #обнуление файла для последующей записи
    open('referat2.txt', 'w').close()

    with open('referat.txt', 'r', encoding='utf-8') as file_data:
        file_text_length = 0
        file_words_count = 0
        for file_string in file_data:
            file_text_length += len(file_string)

            words = file_string.split()
            file_words_count += len(words)

            new_file_string = file_string.replace('.', '!')
            with open('referat2.txt', 'a', encoding='utf-8') as new_file_data:
                new_file_data.write(new_file_string)
        
        print(f'Длина строки в файле: {file_text_length} символов.')
        print(f'Количество слов в файле: {file_words_count}.')
        

if __name__ == "__main__":
    main()
