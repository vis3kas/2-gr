'''#11
#def positive(x):
#   return x > 0

#numbers = input().split()
numbers = list(map(int, numbers))
result = list(filter(positive, numbers))
print(result)

#12

def div_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0

numbers = input().split()
numbers = list(map(int, numbers))
result = list(filter(div_3_or_5, numbers))
print(result)

#13

numbers = input().split()
numbers = list(map(int, numbers))

low, high = input().split()
low = int(low)
high = int(high)

def in_range(x):
    return low <= x <= high

result = list(filter(in_range, numbers))
print(result)

#14

def is_py(name):
    return name.lower().endswith(".py")

files = input().split()
result = list(filter(is_py, files))
print(result)

#15

s = input().split(", ")
def check(i):
    m = i.split()[-1]
    if int(m) >= 60:
        return True
    return False
out = list(filter(check, s))
print(out)

names = [i.split()[0] for i in s]
marks = [i.split()[-1] for i in s]

journal = {}
for i in range(len(names)):
    if int(marks[1]) >= 60:
        journal[names[i]] = int(marks[i])

print(s)
print(names)
#16


    w = i.strip().lower()
    if len(w) >= 2:
        if w[0] == w[-1]:
            return True
        return False
out = list(filter(check, s))
print(out)

#17

s = input().split(",")
def check(i: str):
    return int(i.split()[0]) >= 300 and i[-1] == "1"
out = list(filter(check, s))
print(out)

#18

s = input().split(" ")

def check(i):
    return int(i)

out = list(map(check, s))
print(out)

#19

s = input().split(",")

def check(i):
    return i.strip().capitalize()

out = list(map(check, s))
print(out)

#20

s = input().split()

def check(i):
    return (i[0], i[-1])

out = list(map(check, s))
print(out)

#21

s = input().split()

def check(i):
    sec = int(i)
    minutes = sec // 60
    seconds = sec % 60
    return (minutes, seconds)

out = list(map(check, s))
print(out)

#22

s = input().split()

def check(i):
    return int(i) * 100

out = list(map(check, s))
print(out)

#23

s = input().split(",")

def check(i):
    w = i.split()
    return int(w[0]) * int(w[1])

out = list(map(check, s))
print(out)

#24

s1 = input().split()
s2 = input().split()

def check(i):
    return int(i[0]) - int(i[1])

out = list(map(check, zip(s1, s2)))
print(out)

#25

s = input().split()
#1 map and filter
def check(i):
    return int(i) % 2 != 0

def square(i):
    return int(i) * int(i)

odd_nums = list(filter(check, s))
out1 = list(map(square, odd_nums))
print("filter+map:", out1)
#2 spiski
out2 = [int(i) * int(i) for i in s if int(i) % 2 != 0]
print("spiski:", out2)'''

#26

s = input().split(",")

#1 filter
def check(i):
    w = i.split()
    if int(w[1]) >= 18:
        return True
    return False

def get_name(i):
    return i.split()[0]

adults = list(filter(check, s))
out1 = list(map(get_name, adults))
print("filter+map:", out1)

#2 spiski
out2 = [i.split()[0] for i in s if int(i.split()[1]) >= 18]
print("включение:", out2)

#27

s = input().split()

#1 filter
def check(i):
    if abs(int(i)) > 5:
        return True
    return False

def module(i):
    return abs(int(i))

big_nums = list(filter(check, s))
out1 = list(map(module, big_nums))
print("filter+map:", out1)

#2 spiski
out2 = [abs(int(i)) for i in s if abs(int(i)) > 5]
print("включение:", out2)

#28

s = input().split(",")

#1 filter
def clean(i):
    return i.strip().lower()

def check(i):
    if i.startswith("го"):
        return True
    return False

cleaned = list(map(clean, s))
out1 = list(filter(check, cleaned))
print("filter+map:", out1)

#2 spiski
out2 = [i.strip().lower() for i in s if i.strip().lower().startswith("го")]
print("включение:", out2)

#29

s = input().split()

#1
out1 = [int(i) * int(i) for i in s if int(i) > 0]
print("Сначала фильтр, потом квадрат:", out1)

#2
squared = [int(i) * int(i) for i in s]
out2 = [x for x in squared if x > 0]
print("Сначала квадрат, потом фильтр:", out2)

#30

# 30
s = input().split()

#1
f = filter(bool, s)
print("1-й список (filter bool):", list(f))
print("2-й список (filter bool):", list(f))

print()

#2
m = map(abs, map(int, s))
print("1-й список (map abs):", list(m))
print("2-й список (map abs):", list(m))