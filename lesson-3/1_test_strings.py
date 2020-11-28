from collections import Counter

# Вывести последнюю букву в слове
print('')
print('---- 1 ----')
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
print('')
print('---- 2 ----')
word = 'Архангельск'
letters = Counter(word.lower())
print(f'Количество "а" в слове {word}: {letters["а"]}')


# Вывести количество гласных букв в слове
print('')
print('---- 3 ----')
word = 'Архангельск'
letters = 'аоуэиыеёюя'
sum_letters = 0
for letter in word.lower():
    if letter in letters:
        sum_letters += 1
print(f'Количество гласных в слове {word}: {sum_letters}')


# Вывести количество слов в предложении
print('')
print('---- 4 ----')
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
print( len(sentence_list) )


# Вывести первую букву каждого слова на отдельной строке
print('')
print('---- 5 ----')
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
for word in sentence_list:
    print(word[0])

# Вывести усреднённую длину слова.
print('')
print('---- 6 ----')
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
sum_length = 0
for word in sentence_list:
    sum_length += len(word)
print(sum_length / len(sentence_list))

#Более красивое решение:
print("")
sentence_len = len(sentence.split())
sentence_sum = len(sentence.replace(" ", ""))
print(sentence_sum / sentence_len)
