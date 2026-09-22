# **ЛР2 — Коллекции и матрицы (list/tuple/set/dict)**
## Задание 1
```python
def min_max(user_list):
    """
    Находит минимальный и максимальный элемент списка чисел
    In: принимает от пользователя list[float | int] (проверяет, действительно ли введен список)
    Out: возвращает tuple[float | int, float | int] - с минимальным и максимальным числом;
    Возвращает ошибку ValueError в случае некорректного ввода 
    """
    if not isinstance(user_list, list):
        return 'ValueError'
    try:
        min_el = min(user_list)
        max_el = max(user_list)
        return tuple([min_el, max_el])
    except ValueError:
        return 'ValueError'     
test_data_mm = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]
for test in test_data_mm:
    print(min_max(test))

def unique_sorted(user_list):
    """
    Сортирует список по возрастанию, сохраняя только уникальные элементы
    In: принимает от пользователя list[float | int] (проверяет, действительно ли введен список)
    Out: возвращает list[float | int] c отсортированными уникальными элементами;
    Возвращает ошибку ValueError в случае некорректного ввода 
    """
    if not isinstance(user_list, list):
            return 'ValueError'
    return sorted(list(set(user_list)))
test_data_us = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]
for test in test_data_us:
    print(unique_sorted(test))

def flatten(user_list):
    """
    Разворачивает список списков/кортежей в один плоский список (row-major order)
    In: принимает от пользователя list[list | tuple] (проверяет, действительно ли введен список со списками и кортежами)
    Out: Возвращает 'расплющенный' список с элементами из вложенных кортежей/списков;
    Возвращает ошибку TypeError в случае некорректного ввода
    """
    out_list = []
    try:
        for list_i in user_list:
            if isinstance(list_i, tuple) or isinstance(list_i, list):
                for element in list_i:
                    out_list.append(element)
            else: raise TypeError
        return out_list
    except TypeError:
        return 'TypeError'
test_data_f = [[[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]]
for test in test_data_f:
    print(flatten(test))
```
![01-ex](../../images~/lab02/01-ex-02.png)
## Задание 2
 ```python
 def transpose(matrix):
    """
    Реализует транспонирование матрицы
    In: принимает от пользователя list[list[float | int]] (проверяет, действительно ли введен список)
    Out: возвращает list[list] - транспонированную матрицу;
    Возвращает ValueError в случае некорректного ввода
    """
    if not isinstance(matrix, list):
            return 'ValueError'
    if len(matrix) > 0:
        rows = len(matrix[0])
        t_matrix = []
    else: return '[]'
    try:
        for number_element in range(rows):
            new_row = []
            for row in matrix:
                new_row.append(row[number_element])
            t_matrix.append(new_row)
        return t_matrix
    except IndexError:
        return 'ValueError'
test_data_t = [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]]
for test in test_data_t:
    print(transpose(test))

def row_sums(user_list):
    """
    Находит сумму по каждой строке матрицы
    In: принимает от пользователя list[list[float | int]] (проверяет, действительно ли введен список)
    Out: возвращает list[float] - список с суммами по строкам;
    Возвращает ValueError в случае некорректного ввода
    """
    if not isinstance(user_list, list):
            return 'ValueError'
    list_with_sum = []
    len_row = len(user_list[0])
    try:
        for row in range(len(user_list)):
            sum_row = 0
            for ind in range(len_row):
                sum_row += user_list[row][ind]
            list_with_sum.append(sum_row)
        return list_with_sum
    except IndexError:
        return 'ValueError'
test_data_rs = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
for test in test_data_rs:
    print(row_sums(test))

def col_sums(user_list):
    """
    Находит сумму по каждому столбцу матрицы
    In: принимает от пользователя list[list[float | int]] (проверяет, действительно ли введен список)
    Out: возвращает list[float] - список с суммами по столбцам;
    Возвращает ValueError в случае некорректного ввода
    """
    if not isinstance(user_list, list):
            return 'ValueError'
    list_with_sum = []
    len_row = len(user_list[0])
    try:
        for ind in range(len_row):
            sum_col = 0
            for row in range(len(user_list)):          
                sum_col += user_list[row][ind]
            list_with_sum.append(sum_col)
        return list_with_sum
    except IndexError:
        return 'ValueError'
test_data_cs = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
for test in test_data_rs:
    print(col_sums(test))
```
![ex-2](../../images~/lab02/02-ex-02.png)