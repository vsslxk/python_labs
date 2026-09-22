n = int(input('in_1: '))
a = 0
b = 0
for i in range(n):
    user = input(f'in_{i+2}: ')
    if user[-5:] == 'False': b += 1
    if user[-4:] == 'True': a += 1
print('out: ' + str(a) + ' ' + str(b))