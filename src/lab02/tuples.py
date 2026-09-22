def format_record(user_tuple):
    fio = user_tuple[0]
    group = user_tuple[1]
    gpa = user_tuple[2]
    return fio+group
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))