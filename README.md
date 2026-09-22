# python_labs
## **ЛР1 — Ввод/вывод и форматирование**
### Задание 1
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![ex-1](images~/lab01/01-ex.png)
### Задание 2
```python
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
summ = a+b
avg = round(summ/2,2)
print(f'sum={round(summ,2)}; avg={avg}')
```
![ex-2](images~/lab01/02-ex.png)
### Задание 3
```python
price = float(input('price='))
discount = float(input('discount='))
vat = float(input('vat='))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
![ex-3](images~/lab01/03-ex.png)
### Задание 4
```python
minutes = int(input('Минуты: '))
hours = minutes//60
minutes = minutes%60
print(f'{hours}:{minutes:02d}')
```
![ex-4](images~/lab01/04-ex.png)
### Задание 5
```python
fio = input('ФИО: ')
initials = ''.join([x for x in fio if x.isupper()])
len_fio = len([x for x in fio if x != ' '])+2
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {len_fio}')
```
![ex-5](images~/lab01/05-ex.png)
### Задание 6
```python
n = int(input())
a = 0
b = 0
for i in range(n):
    user = input()
    if user[-5:] == 'False': b += 1
    if user[-4:] == 'True': a += 1
print(a,b)
```
![ex-6](images~/lab01/06-ex.png)
### Задание 7
```python
in0 = input('in: ')
out = ''
first_letter = 0
for i in in0:
    if i.isupper():
        out += i
        first_letter = in0.index(i)
        break
in1 = in0[first_letter:]
flag = False
for i in in1:
    if flag:
        out += i
        difference = in0.index(i)-first_letter
        break
    if i.isdigit():
        flag = True
in2 = in1[difference:]
for i in range(len(in2)):
    if i%difference == 0 and i!=0:
        out+=in2[i]  
print(f'out: {out}')
```
![ex-7](images~/lab01/07-ex.png)

## **ЛР2 — Коллекции и матрицы (list/tuple/set/dict)**
### Задание 1
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
![01-ex](images~/lab02/01-ex-02.png)
### Задание 2
![Код, результат работы программы](images~/lab01/lab02/02_ex_01.png) 
![Код, результат работы программы](images~/lab01/lab02/02_ex_02.png) 
![Код, результат работы программы](images~/lab01/lab02/02_ex_03.png)