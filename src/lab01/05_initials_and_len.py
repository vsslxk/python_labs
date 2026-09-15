fio = input('ФИО: ')
initials = ''.join([x for x in fio if x.isupper()])
len_fio = len([x for x in fio if x != ' '])+2
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {len_fio}')



