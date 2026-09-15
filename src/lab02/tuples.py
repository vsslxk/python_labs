info_tuple = (" ", "ABB-01", '3.999')
group = info_tuple[1]
gpa = info_tuple[2]
if not isinstance(gpa, (float, int)): raise ValueError
f_i_o = fio.split()
if len(f_i_o) == 3: fio_s = f_i_o[0][0].upper() + f_i_o[0][1:] + ' ' + f_i_o[1][0].upper() + '. ' + f_i_o[2][0].upper() + '., '
elif len(f_i_o) == 2: fio_s = f_i_o[0][0].upper() + f_i_o[0][1:] + '., '
group_s = 'гр. ' + group + ', '
gpa_s = 'GPA ' + str(f'{gpa:.2f}')
all_s = fio_s + group_s + gpa_s
print(all_s)