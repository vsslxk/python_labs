n = int(input())
a = 0
b = 0
for i in range(n):
    user = input()
    if user[-5:] == 'False': b += 1
    if user[-4:] == 'True': a += 1
print(a,b)