##1

n = int(input("n = "))
a = []
for i in range(1, n + 1):
    a.append(i)
print(a)

##2

n = int(input("n = "))
a = []
for i in range(n + 1):
    a.append(i * i)
print(a)

##3

a = []
while True:
    s = input()
    if s == "стоп":
        break
    a.append(int(s))
print(len(a))

##4

a = [3, -1, 4, 0]
s = 0
for x in a:
    s += x
print(s)

##5

a = [3, -1, 4, 0]
s = 0
for x in a:
    s += x
print(s)

##6

a = [2, -3, 0, 4]
p = 1
for x in a:
    p *= x
print(p)

##7

a = [2, 0, -3, 5, 0]
pos = neg = zero = 0
for x in a:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        zero += 1
print(pos, neg, zero)

##8

a = [5, 2, 0, 2, -4]
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
print(b)

##9

a = [3, -2, 0, -7, 5]
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
print(a)

##10

a = [1, 2, 3, 4]
s = 0
for x in a:
    s += x
sr = s / len(a)

b = []
for x in a:
    if x > sr:
        b.append(x)
print(b)

##11

a = [10, 20, 30, 40]

print(a[0], a[len(a) - 1])
print(a[-1], a[-len(a)])

##12

a = [10, 20, 30]
for i, x in enumerate(a):
    print(x, i, i - len(a))

##13

a = [10, 20, 30]
i = int(input("i = "))

if -len(a) <= i < len(a):
    print(a[i])
else:
    print("Нет такого индекса")

##14

a = [1, 2, 3, 4]
if len(a) >= 2:
    tmp = a[0]
    a[0] = a[-1]
    a[-1] = tmp
print(a)

##15

a = [1, 2, 3, 4, 5]
n = len(a)

if n == 0:
    print("Центра нет")
elif n % 2 == 1:
    print(a[n // 2])
else:
    print(a[n // 2 - 1], a[n // 2])

##16

a = [10, 20, 30, 40]

for i in range(-1, -len(a) - 1, -1):
    print(a[i])

for i in range(len(a) - 1, -1, -1):
    print(a[i])

i = len(a) - 1
while i >= 0:
    print(a[i])
    i -= 1

##17

a = [1, 4, 3, 8, 5]

po_index = []
po_value = []
for i in range(len(a)):
    if i % 2 == 0:
        po_index.append(a[i])
    if a[i] % 2 == 0:
        po_value.append(a[i])

print(po_index)
print(po_value)

##18

a = [3, 8, 2, 5]
b = []
for i in range(len(a) - 1):
    b.append(a[i] + a[i + 1])
print(b)

##19

a = [1, 4, 2, 5, 3]
res = []
for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        res.append(i)
print(res)

##20

a = [10, 20, 30, 40, 50]
n = len(a)

i = 0
j = n - 1
while i < j:
    print(f"({i}, {j}): {a[i]} и {a[j]}")
    i += 1
    j -= 1

if i == j:
    print(f"центр: индекс {i}, значение {a[i]}")