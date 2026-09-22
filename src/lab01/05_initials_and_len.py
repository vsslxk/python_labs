fio = input('ФИО: ')
fio = ' ' + fio
initials = ''.join([fio[x].upper() for x in range(1, len(fio)) if fio[x].isalpha() and  not fio[x-1].isalpha()])
len_fio = len([x for x in fio if x != ' '])+2
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {len_fio}')



