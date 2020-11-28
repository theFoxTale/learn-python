"""

Домашнее задание №2

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare_strings(str1, str2):
  if not isinstance(str1, str) or not isinstance(str2, str):
      return 0
  if str1 == str2:
      return 1
  if str2 == 'learn':
      return 3
  if len(str1) > len(str2):
      return 2
  return 'not specified'


def print_str_comparison(s1, s2):
  cs = compare_strings(s1, s2)
  return f"String 1 = '{s1}', string 2 = '{s2}': {cs}"
    

if __name__ == "__main__":
    print(print_str_comparison("sample string", 3))
    print(print_str_comparison("sample string", "sample string"))
    print(print_str_comparison("other sample string", "sample string"))
    print(print_str_comparison("sample string", "other sample string"))
    print(print_str_comparison("sample string", "learn"))
    