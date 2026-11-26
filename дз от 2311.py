#0

a, b, c = map(float, input("введите 3 числа: ").split())
average = (a + b + c) / 3
print(f"ср арифм = {average:.2f}")

#1

name = input()
age = int(input())

print(f"Меня зовут {name}, мне {age} лет.")

#2

name = input()
city = input()
subject = input()
print(f"имя: {name}")
print(f"город: {city}")
print(f"любимый предмет: {subject}")

#3

a = int(input())
b = int(input())

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")

#4

prod = input()
price = float(input())

print(f"товар: {prod}, цена: {price} руб")

#5

a, b, c = map(float, input("введите 3 оценки: ").split())
average = (a + b + c) / 3
print(f"ср балл = {average:.2f}")

#6

c = float(input())
f = c * 9 / 5 + 32

print(f"{c:.1f} °C = {f:.1f} °F")

#7

prod = input()
price = float(input())
count = float(input())
total = price * count
print(f"{prod}: {count} шт. * {price:.2f} руб. = {total:.2f} руб.")
#8

price = float(input())
dis_per = float(input())

dis_rub = price * dis_per / 100
fin_price = price - dis_rub

print(f" цена: {price:.2f} руб.")
print(f" скидка: {dis_rub:.2f} руб.")
print(f" цена: {fin_price:.2f} руб.")

#9

done = int(input())
total = int(input())
per = done / total * 100
print(f"выполнено: {per:.1f}")

#10

num = int(input())
print(f"заказ №{num:06d}")

#11

h = int(input())
m = int(input())
s = int(input())
print(f"{h:02}:{m:02}:{s:02}")

#12

name = input()
diff = float(input())
print(f"{name}: {diff:+.2f} сек.")

#13

word = input()
print(f"|{word:<20}|")
print(f"|{word:^20}|")
print(f"|{word:>20}|")

#14

word = input()
print(f"{word:=^30}")

#15

name = input()
price = float(input())
print(f"{name:<20} {price:>10.2f}")

#16

n1 = input()
p1 = float(input())
n2 = input()
p2 = float(input())
n3 = input()
p3 = float(input())

print(f"{'товар':<20} {'цена':>10}")
print(f"{n1:<20} {p1:>10.2f}")
print(f"{n2:<20} {p2:>10.2f}")
print(f"{n3:<20} {p3:>10.2f}")

#17

amount = int(input())
print(f"на счёте: {amount:,} руб.")

#18

num = int(input())
print(f"десятичная: {num}")
print(f"двоичная: {num:b}")
print(f"шестнадцатеричная: {num:x}")

#19

name1 = input()
price1 = float(input())
count1 = int(input())

name2 = input()
price2 = float(input())
count2 = int(input())

total1 = price1 * count1
total2 = price2 * count2
total = total1 + total2

print(f"{'товар':<15} {'кол-во':>6} {'цена':>10} {'стоимость':>12}")

print(f"{name1:<15} {count1:>6} {price1:>10.2f} {total1:>12.2f}")
print(f"{name2:<15} {count2:>6} {price2:>10.2f} {total2:>12.2f}")

print(f"{'итого:':<15} {'':>6} {'':>10} {total:>12.2f}")

#20

n = int(input())

print(f"{'число':>10} {'квадрат':>10} {'куб':>10}")

for i in range(1, n + 1):
    print(f"{i:>10} {i * i:>10} {i * i * i:>10}")
