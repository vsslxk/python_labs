# python_labs
## **Лаба №1**
### Задание 1
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![ex-1](../../images~/lab01/01-ex.png)
### Задание 2
```python
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
summ = a+b
avg = round(summ/2,2)
print(f'sum={round(summ,2)}; avg={avg}')
```
![ex-2](../../images~/lab01/02-ex.png)
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
![ex-3](../../images~/lab01/03-ex.png)
### Задание 4
```python
minutes = int(input('Минуты: '))
hours = minutes//60
minutes = minutes%60
print(f'{hours}:{minutes:02d}')
```
![ex-4](../../images~/lab01/04-ex.png)
### Задание 5
```python
fio = input('ФИО: ')
initials = ''.join([x for x in fio if x.isupper()])
len_fio = len([x for x in fio if x != ' '])+2
print(f'Инициалы: {initials}.')
print(f'Длина (символов): {len_fio}')
```
![ex-5](../../images~/lab01/05-ex.png)
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
![ex-6](../../images~/lab01/06-ex.png)
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
![ex-7](../../images~/lab01/07-ex.png)