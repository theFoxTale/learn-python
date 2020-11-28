"""

Домашнее задание №3

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def middle_score(scores_list):
  middle = sum(scores_list) / len(scores_list)
  return round(middle, 2)

def main(classes):
    school_score = []
    print('Средний бал по классам:')
    for one_class in classes:
      one_class['middle_score'] = middle_score(one_class['class_scores'])
      print(f"Класс {one_class['class_name']}: {one_class['middle_score']}")
      school_score.append( one_class['middle_score'] )
    
    print('')
    print(f'Средний бал по школе: {middle_score(school_score)}')


school_classes = [
  {'class_name': '5А', 'class_scores': [3,4,4,5,2]},
  {'class_name': '5Б', 'class_scores': [4,4,5,3,2,5,4]},
  {'class_name': '6А', 'class_scores': [5,5,3,5,4,2]},
  {'class_name': '7А', 'class_scores': [4,4,3,5,5,5,3]},
  {'class_name': '7Б', 'class_scores': [4,3,3,2,5]},
]

if __name__ == "__main__":
    main(school_classes)
    