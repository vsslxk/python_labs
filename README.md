# python_labs
## **Лаба №1**
### Задание 1
```
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![ex-1](images~/lab01/01-ex.png)
### Задание 2
```
a = float(input('a: ').replace(',', '.'))
b = float(input('b: ').replace(',', '.'))
summ = a+b
avg = round(summ/2,2)
print(f'sum={round(summ,2)}; avg={avg}')
```
![ex-2](images~/lab01/02-ex.png)
### Задание 3
```
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
![Код, результат работы программы](images~/lab01/04_ex.png)
### Задание 5
![Код, результат работы программы](images~/lab01/05_ex.png)
### Задание 6
![Код, результат работы программы](<images~/lab01/06_ex (2).png>)
### Задание 7
![Код, результат работы программы](images~/lab01/07_ex.png)

## **Лаба №2**
### Задание 1
![Код, результат работы программы](images~/lab01/lab02/01_ex_02.png)
![Код, результат работы программы](images~/lab01/lab02/01_ex_02_2.png)
### Задание 2
![Код, результат работы программы](images~/lab01/lab02/02_ex_01.png) 
![Код, результат работы программы](images~/lab01/lab02/02_ex_02.png) 
![Код, результат работы программы](images~/lab01/lab02/02_ex_03.png)