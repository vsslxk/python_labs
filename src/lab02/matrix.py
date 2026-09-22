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
            
            
                