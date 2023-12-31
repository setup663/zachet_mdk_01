'''
Пример билета и решения.
21-22-23-24-25-ис-21, КМПО, МДК.01.01.
Преподаватель: Гусятинер Л.Б., 05.12.2022
'''
'''
В базе данных хранятся сведения о работе библиотеки: дата текущего года,
фамилия читателя, количество книг
Структура входного файла in.txt
23.10.2022 Винни-Пух 5
12.11.2022 Винни-Пух 3
15.10.2022 Пятачок 7
...
Определить количество книг, взятых каждым читателем за все время, упорядочив
по фамилии читателя
Структура выходного файла out.txt
Читатель Количество
Винни-Пух 8
Пятачок 7
'''
from file_parcer import Parcer
from sorting import Sorter
parser = Parcer()
sorter = Sorter()
not_sorted = parser.parcing('in.txt')
sorter.sorting(not_sorted, 'out.txt')