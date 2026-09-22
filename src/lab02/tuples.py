def format_record(user_tuple):
    fio = user_tuple[0]
    group = user_tuple[1]
    gpa = user_tuple[2]
    # Обработка ФИО
    name_surname_fat = fio.split()
    if len(name_surname_fat) == 3: fio = name_surname_fat[0][0].upper() + name_surname_fat[0][1:] + ' ' + name_surname_fat[1][0].upper() + '.' + name_surname_fat[2][0].upper() +'.'
    else: fio = name_surname_fat[0] + ' ' + name_surname_fat[1][0].upper() + '.'
    # Обработка группы
    group = 'гр. ' + group
    # Обработка GPA
    gpa = f'GPA {gpa:.2f}'
    return fio + ', ' + group + ', ' + gpa
data = [("Иванов Иван Иванович", "BIVT-25", 4.6), ("Петров Пётр", "IKBO-12", 5.0), ("Петров Пётр Петрович", "IKBO-12", 5.0), ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)]
for test in data:
    print(format_record(test))