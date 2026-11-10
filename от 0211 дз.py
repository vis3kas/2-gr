##1

marks = {
    "Анна": 5,
    "Иван": 3,
    "Олег": 4
}

print("Оценка Ивана:", marks["Иван"])

marks["Иван"] = 4

marks["Мария"] = 5

del marks["Олег"]

print("Студентов:", len(marks))
for name, mark in marks.items():
    print(f"{name}: {mark}")

##2

phones = {
    "Анна": "+7 900 111-11-11",
    "Иван": "+7 900 222-22-22",
    "Олег": "+7 900 333-33-33"
}

name = input("Имя контакта: ")

if name in phones:
    print("Телефон:", phones[name])
else:
    print("Контакт не найден")
    number = input("Введите номер: ")
    phones[name] = number

print("\nТелефонная книга:")
for n, p in phones.items():
    print(f"{n}: {p}")

##3

prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 150,
    "яблоко": 30
}

product = input("Товар: ").lower()
count = int(input("Количество: "))

if product in prices:
    total = prices[product] * count
    print("Стоимость:", total)
else:
    print("Товар не найден")

print("\nТовары не дороже 100 рублей:")
for name, price in prices.items():
    if price <= 100:
        print(f"{name}: {price}")

##4

marks = {
    "Анна": 5,
    "Иван": 3,
    "Олег": 4,
    "Мария": 5,
    "Пётр": 2
}

if len(marks) == 0:
    print("Нет данных")
else:

    total = 0
    for m in marks.values():
        total += m
    avg = total / len(marks)
    print("Средняя оценка:", avg)

    print("Отличники:")
    for name, m in marks.items():
        if m == 5:
            print(name)

    low = 0
    for m in marks.values():
        if m < 4:
            low += 1
    print("Оценка ниже 4 у", low, "студентов")

    good = {}
    for name, m in marks.items():
        if m >= 4:
            good[name] = m
    print("Успевающие:", good)

##5

text = input("Текст: ").lower()

words = text.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

for w, c in freq.items():
    print(f"{w}: {c}")

##6

warehouse_1 = {"ручка": 10, "тетрадь": 5}
warehouse_2 = {"ручка": 7, "карандаш": 12}

total = {}

for name, cnt in warehouse_1.items():
    total[name] = cnt

for name, cnt in warehouse_2.items():
    if name in total:
        total[name] += cnt
    else:
        total[name] = cnt

print("Объединённый склад:", total)

all_items = 0
for cnt in total.values():
    all_items += cnt
print("Всего единиц:", all_items)

print("Склад 1:", warehouse_1)
print("Склад 2:", warehouse_2)

##7

journal = {
    "Анна": [5, 4, 5],
    "Иван": [3, 4, 3],
    "Олег": [4, 5, 4],
    "Мария": []
}

averages = {}
no_marks = []

for name, marks in journal.items():
    if len(marks) == 0:
        no_marks.append(name)
        continue
    s = 0
    for m in marks:
        s += m
    avg = s / len(marks)
    averages[name] = avg

print("Средние оценки:")
for name, avg in averages.items():
    print(f"{name}: {avg:.2f}")

for name in no_marks:
    print(f"{name}: нет оценок")

print("Средняя не ниже 4:")
for name, avg in averages.items():
    if avg >= 4:
        print(name)

if len(averages) == 0:
    print("Нет данных")
else:
    best = None
    for avg in averages.values():
        if best is None or avg > best:
            best = avg
    print("Максимальная средняя:", best)
    print("Лучшие студенты:")
    for name, avg in averages.items():
        if avg == best:
            print(name)

##8

student = {
    "id": 101,
    "name": "Анна",
    "age": 18,
    "is_active": True,
    "marks": [5, 4, 5, 4],
    "address": {
        "city": "Москва",
        "street": "Лесная"
    },
    "phone": None
}

print("Имя:", student["name"])
print("Возраст:", student["age"])
print("Город:", student["address"]["city"])

student["marks"].append(5)

s = 0
for m in student["marks"]:
    s += m
student["average"] = s / len(student["marks"])

student["address"]["city"] = "Казань"

student["phone"] = input("Телефон: ")

student["has_scholarship"] = student["is_active"] and student["average"] >= 4.5

print("\nКарточка студента:")
for key, value in student.items():
    print(f"{key}: {value}")

##9

product = {
    "id": 42,
    "title": "Наушники",
    "price": 3500,
    "in_stock": True,
    "tags": ["техника", "звук"],
    "specs": {
        "wireless": True,
        "battery_hours": 30,
        "color": "чёрный"
    },
    "reviews": [
        {"author": "Иван", "rating": 5, "text": "Хороший звук"},
        {"author": "Ольга", "rating": 4, "text": "Удобные"}
    ]
}

print("Название:", product["title"])
print("Цена:", product["price"])
print("Цвет:", product["specs"]["color"])
print("Время работы:", product["specs"]["battery_hours"], "ч")

product["price"] = product["price"] * 0.9
print("Новая цена:", product["price"])

if "скидка" not in product["tags"]:
    product["tags"].append("скидка")

product["reviews"].append({"author": "Анна", "rating": 3, "text": "Быстро разряжаются"})

s = 0
for r in product["reviews"]:
    s += r["rating"]
product["rating"] = s / len(product["reviews"])

print("Отзывы ниже 4:")
for r in product["reviews"]:
    if r["rating"] < 4:
        print(r["author"])

if product["in_stock"] and product["specs"]["wireless"]:
    print("Можно заказать")
else:
    print("Не подходит")

##10

order = {
    "number": "A-102",
    "customer": {
        "name": "Максим",
        "email": "max@example.com"
    },
    "items": [
        {"title": "Тетрадь", "price": 80, "quantity": 3},
        {"title": "Ручка", "price": 50, "quantity": 2}
    ],
    "delivery": {
        "method": "курьер",
        "price": 200
    },
    "paid": False,
    "comment": None
}

print("Заказ:", order["number"])
print("Покупатель:", order["customer"]["name"])

print("\nПозиции:")
items_total = 0
for item in order["items"]:
    cost = item["price"] * item["quantity"]
    items_total += cost
    print(f"{item['title']}: {item['quantity']} x {item['price']} = {cost}")

print("Стоимость товаров:", items_total)

if items_total >= 1000:
    order["delivery"]["price"] = 0

order["total"] = items_total + order["delivery"]["price"]
print("Итого с доставкой:", order["total"])

if order["paid"]:
    print("Заказ оплачен")
else:
    print("Ожидает оплаты")

if order["comment"] is None:
    print("Комментария нет")

order["items"][0]["quantity"] = 12

items_total = 0
for item in order["items"]:
    items_total += item["price"] * item["quantity"]

if items_total >= 1000:
    order["delivery"]["price"] = 0

order["total"] = items_total + order["delivery"]["price"]

print("\nПосле изменения количества тетрадей:")
print("Стоимость товаров:", items_total)
print("Доставка:", order["delivery"]["price"])
print("Итого:", order["total"])