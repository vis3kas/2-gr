##1

s = input()
code = ord(s)
print(code)
print(chr(code - 1))
print(chr(code + 1))

##2

s = input()
c1, c2 = s.split()

k1 = ord(c1)
k2 = ord(c2)

if k1 > k2:
    k1, k2 = k2, k1
print(k2 - k1 - 1)

##3

s = input("Строка: ")
k = int(input("Сдвиг: "))

res = ""
for c in s:
    if 'a' <= c <= 'z':
        new_code = ord('a') + (ord(c) - ord('a') + k) % 26
        res += chr(new_code)
    else:
        res += c
print(res)

##4

import string

s = input("Строка: ")

letters = digits_cnt = punct = other = 0
for c in s:
    if c in string.ascii_letters:
        letters += 1
    elif c in string.digits:
        digits_cnt += 1
    elif c in string.punctuation:
        punct += 1
    else:
        other += 1

print("букв", letters)
print("цифр", digits_cnt)
print("знаков", punct)
print("остальных", other)

##5

import string

p = input("Пароль: ")

has_lower = False
has_upper = False
has_digit = False
has_punct = False
has_space = False

for c in p:
    if c in string.ascii_lowercase:
        has_lower = True
    if c in string.ascii_uppercase:
        has_upper = True
    if c in string.digits:
        has_digit = True
    if c in string.punctuation:
        has_punct = True
    if c == ' ':
        has_space = True

problems = []
if len(p) < 8:
    problems.append("длина меньше 8")
if not has_lower:
    problems.append("нет строчной буквы")
if not has_upper:
    problems.append("нет заглавной буквы")
if not has_digit:
    problems.append("нет цифры")
if not has_punct:
    problems.append("нет знака пунктуации")
if has_space:
    problems.append("есть пробел")

if not problems:
    print("Подходит")
else:
    print("Не подходит:")
    for x in problems:
        print("-", x)

##6

s = input()
i = 0
while i < len(s) and s[i] == ' ':
    i += 1
j = len(s) - 1
while j >= 0 and s[j] == ' ':
    j -= 1
s = s[i:j+1]
res = ""
prev_space = False
for c in s:
    if c == ' ':
        if not prev_space:
            res += c
        prev_space = True
    else:
        res += c
        prev_space = False
print(res)

##8

s = input("Строка: ").lower()

clean = ""
for c in s:
    if c.isalnum():
        clean += c

ok = True
i = 0
j = len(clean) - 1
while i < j:
    if clean[i] != clean[j]:
        ok = False
        break
    i += 1
    j -= 1

print("Да" if ok else "Нет")

##9

s = input("Строка: ")

if s == "":
    print("")
else:
    res = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res += s[i - 1] + str(count)
            count = 1
    res += s[-1] + str(count)
    print(res)