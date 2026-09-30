def format_record(user_tuple):
    """
    Реализует необходимую функцию, преобразующую кортеж в строку установленного вида
    In: принимает от пользователя tuple[str, str, float] (проверяет, действительно ли введен кортеж)
    Out: возвращает str - строку с информацией о студенте;
    Возвращает ошибку ValueError в случае некорректного ввода(неверный тип GPA, пустое ФИО, пустая группа) 
    """
    if not isinstance(user_tuple, tuple):
        return 'ValueError'
    try:
        fio = user_tuple[0]
        group = user_tuple[1]
        gpa = user_tuple[2]
        if len(user_tuple) > 3:
            raise ValueError
        # Обработка ФИО
        name_surname_fat = fio.split()
        if len(name_surname_fat) == 3: fio = name_surname_fat[0][0].upper() + name_surname_fat[0][1:] + ' ' + name_surname_fat[1][0].upper() + '.' + name_surname_fat[2][0].upper() +'.'
        else: fio = name_surname_fat[0] + ' ' + name_surname_fat[1][0].upper() + '.'
        # Обработка группы
        if len(group) == 0:
            raise ValueError
        group = 'гр. ' + group
        # Обработка GPA
        if int(gpa) > 5 or int(gpa) < 0:
            raise ValueError
        gpa = f'GPA {gpa:.2f}'
        return fio + ', ' + group + ', ' + gpa
    except IndexError:
        return "ValueError"
data = [("Иванов Иван Иванович", "BIVT-25", 4.6), ("Петров Пётр", "IKBO-12", 5.0), ("Петров Пётр Петрович", "IKBO-12", 5.0), ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)]
for test in data:
    try: print(format_record(test))
    except ValueError: print('ValueError')