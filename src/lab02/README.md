# **ЛР2 — Коллекции и матрицы (list/tuple/set/dict)**
## Задание 1
```python
def min_max(user_list):
    '''Получаю на вход список чисел пользователя и нахожу минимальный и максимальный элемент'''
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
    '''Принимаю список чисел от пользователя и через множества вывожу уникальные возрастающие элементы'''
    return sorted(list(set(user_list)))
test_data_us = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]
for test in test_data_us:
    print(unique_sorted(test))

def flatten(user_list):
    '''Принимаю на вход список списков(кортежей) пользователя и вывожу в общем списке в row-major order'''
    out_list = []
    try:
        for list_i in user_list:
            if isinstance(list_i, tuple) or isinstance(list_i, list):
                for element in list_i:
                    out_list.append(element)
            else: 'q'*'q'
        return out_list
    except TypeError:
        return 'TypeError'
test_data_f = [[[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]]
for test in test_data_f:
    print(flatten(test))
```
![01-ex](../../images~/lab02/01-ex-02.png)