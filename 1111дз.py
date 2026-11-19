#1

name = input()
print(name.capitalize())

#2

word = input()
print(word.upper())

#3

text = input()
print(text.strip())

#4

text = input()
print(text.replace(" ", "_"))

#5

text = input().lower()
count = 0
for ch in text:
    if ch == "а":
        count += 1
print(count)

#6

text = input()
word = input()
if word in text:
    print("Да")
else:
    print("Нет")

#7

file = input()
if file.endswith(".txt"):
    print("Да")
else:
    print("Нет")

#8

text = input().lower()
vowels = "аеёиоуыэюя"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print(count)

#9

text = input()
count = 0
for ch in text:
    if ch.isdigit():
        count += 1
print(count)

#10

text = input()
words = text.split()
print(len(words))

#11

text = input()
words = text.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)

#12

text = input()

#1 цикл
rev = ""
for ch in text:
    rev = ch + rev
print("Цикл:", rev)

#2 срез
print("Срез:", text[::-1])

#13

text = input()
sym = input()
print(text.replace(sym, ""))

#14

text = input()
result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].upper()
    else:
        result += text[i].lower()
print(result)

#15

text = input()
clean = ""
for ch in text:
    if ch.isalpha() or ch.isdigit():
        clean += ch.lower()

rev = clean[::-1]

if clean == rev:
    print("Палиндром")
else:
    print("Не палиндром")

#16

text = input()
letters = 0
digits = 0
spaces = 0
other = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        other += 1

print("Букв:", letters)
print("Цифр:", digits)
print("Пробелов:", spaces)
print("Остальных:", other)

#17

text = input()
result = ""
for ch in text:
    if ch not in result:
        result += ch
print(result)

#18

text = input()
words = text.split()
for w in words:
    if w.lower().startswith("а"):
        print(w)

#19

text = input().lower()
clean_text = ""
for ch in text:
    if ch.isalpha() or ch == " ":
        clean_text += ch

words = clean_text.split()
best_word = ""
best_count = 0

for w in words:
    count = words.count(w)
    if count > best_count:
        best_count = count
        best_word = w

print(best_word)

#20

password = input()
ok = True

if len(password) < 8:
    print("длина меньше 8")
    ok = False

has_upper = False
has_lower = False
has_digit = False
has_space = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch == " ":
        has_space = True

if not has_upper:
    print("нет заглавной буквы")
    ok = False
if not has_lower:
    print("нет строчной буквы")
    ok = False
if not has_digit:
    print("нет цифры")
    ok = False
if has_space:
    print("есть пробел")
    ok = False

if ok:
    print("Пароль подходит")