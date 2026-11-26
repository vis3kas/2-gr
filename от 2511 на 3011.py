#1

grades = {}
for line in open("grades.txt", encoding="utf-8"):
    if line.strip() != "":
        name, mark = line.strip().split("|")
        if name not in grades:
            grades[name] = []
        grades[name].append(int(mark))

report = []
for name in grades:
    marks = grades[name]
    avg = sum(marks) / len(marks)
    report.append([name, len(marks), avg])

report.sort(key=lambda x: (-x[2], x[0]))

f = open("report.txt", "w", encoding="utf-8")
for row in report:
    f.write(f"{row[0]}|{row[1]}|{row[2]:.2f}\n")
f.close()

#2

prices = {}
for line in open("prices.txt", encoding="utf-8"):
    if line.strip() != "":
        name, price = line.strip().split("|")
        prices[name] = int(price)

basket = {}
missing = []
for line in open("basket.txt", encoding="utf-8"):
    if line.strip() != "":
        name, count = line.strip().split("|")
        count = int(count)
        if name in prices:
            if name not in basket:
                basket[name] = 0
            basket[name] += count
        else:
            if name not in missing:
                missing.append(name)

f = open("receipt.txt", "w", encoding="utf-8")
total = 0
for name in basket:
    cost = prices[name] * basket[name]
    total += cost
    f.write(f"{name}|{basket[name]}|{cost}\n")
f.write(f"Итого|{total}\n")
f.close()

f = open("missing.txt", "w", encoding="utf-8")
for name in missing:
    f.write(name + "\n")
f.close()

#3

opened = {}
errors = []
lines = open("requests.txt", encoding="utf-8").readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    if line == "": continue
    parts = line.split("|")

    if parts[0] == "OPEN":
        if parts[1] in opened:
            errors.append(f"{i + 1}|{line}")
        else:
            opened[parts[1]] = parts[2]
    elif parts[0] == "CLOSE":
        if parts[1] in opened:
            del opened[parts[1]]
        else:
            errors.append(f"{i + 1}|{line}")

f = open("pending.txt", "w", encoding="utf-8")
for num in sorted(opened.keys(), key=int):
    f.write(f"{num}|{opened[num]}\n")
f.close()

f = open("errors.txt", "w", encoding="utf-8")
for err in errors:
    f.write(err + "\n")
f.close()

#4

records = {}
for line in open("records.txt", encoding="utf-8"):
    if line.strip() != "":
        name, score = line.strip().split("|")
        records[name] = int(score)

for line in open("attempts.txt", encoding="utf-8"):
    if line.strip() != "":
        name, score = line.strip().split("|")
        score = int(score)
        if name not in records or score > records[name]:
            records[name] = score

items = list(records.items())
items.sort(key=lambda x: (-x[1], x[0]))

f = open("records.txt", "w", encoding="utf-8")
for name, score in items:
    f.write(f"{name}|{score}\n")
f.close()

#5

text = open("article.txt", encoding="utf-8").read().lower()
clean_text = ""
for ch in text:
    if ch.isalpha():
        clean_text += ch
    else:
        clean_text += " "

words = clean_text.split()
freq = {}
for w in words:
    if w not in freq:
        freq[w] = 0
    freq[w] += 1

items = list(freq.items())
items.sort(key=lambda x: (-x[1], x[0]))

f = open("top_words.txt", "w", encoding="utf-8")
for i in range(min(5, len(items))):
    f.write(f"{items[i][0]}|{items[i][1]}\n")
f.close()

#6

old = {}
for line in open("notes_old.txt", encoding="utf-8"):
    if line.strip() != "":
        num, text = line.strip().split("|", 1)
        old[num] = text

new = {}
for line in open("notes_new.txt", encoding="utf-8"):
    if line.strip() != "":
        num, text = line.strip().split("|", 1)
        new[num] = text

all_nums = list(set(old.keys()) | set(new.keys()))
all_nums.sort(key=int)

changed = []
f = open("notes.txt", "w", encoding="utf-8")
for num in all_nums:
    if num in new:
        f.write(f"{num}|{new[num]}\n")
        if num in old and old[num] != new[num]:
            changed.append(num)
    else:
        f.write(f"{num}|{old[num]}\n")
f.close()

f = open("changed.txt", "w", encoding="utf-8")
for num in changed:
    f.write(num + "\n")
f.close()

#7

stats = {}
for line in open("matches.txt", encoding="utf-8"):
    if line.strip() != "":
        p1, p2, res = line.strip().split("|")
        if p1 not in stats: stats[p1] = [0, 0, 0]
        if p2 not in stats: stats[p2] = [0, 0, 0]

        stats[p1][0] += 1
        stats[p2][0] += 1

        if res == "X":
            stats[p1][1] += 1
            stats[p1][2] += 3
        elif res == "O":
            stats[p2][1] += 1
            stats[p2][2] += 3
        else:
            stats[p1][2] += 1
            stats[p2][2] += 1

items = list(stats.items())
items.sort(key=lambda x: (-x[1][2], -x[1][1], x[0]))

f = open("leaders.txt", "w", encoding="utf-8")
for name, s in items:
    f.write(f"{name}|{s[0]}|{s[1]}|{s[2]}\n")
f.close()

#8

def save_game(board, turn):
    f = open("save.txt", "w", encoding="utf-8")
    for row in board:
        f.write("".join(row) + "\n")
    f.write(turn + "\n")
    f.close()

def load_game():
    try:
        f = open("save.txt", encoding="utf-8")
        lines = f.read().splitlines()
        f.close()
    except:
        print("сохранение не найдено")
        return

    if len(lines) != 4:
        print("сохранение повреждено")
        return

    turn = lines[3]
    cx = 0
    co = 0
    for row in lines[:3]:
        cx += row.count("X")
        co += row.count("O")

    if (cx == co and turn != "X") or (cx == co + 1 and turn != "O") or (cx + co == 9):
        print("сохранение повреждено")
    else:
        print("всё ок, ход:", turn)

#9

stock = {}
for line in open("stock.txt", encoding="utf-8"):
    if line.strip() != "":
        name, count = line.strip().split("|")
        stock[name] = int(count)

rejected = []
lines = open("operations.txt", encoding="utf-8").readlines()

for i in range(len(lines)):
    line = lines[i].strip()
    if line == "": continue
    parts = line.split("|")

    if len(parts) != 3 or parts[0] not in ["IN", "OUT"] or not parts[2].isdigit():
        rejected.append(f"{i + 1}|FORMAT")
        continue

    cmd = parts[0]
    name = parts[1]
    count = int(parts[2])

    if cmd == "IN":
        if name not in stock: stock[name] = 0
        stock[name] += count
    else:
        if name not in stock: stock[name] = 0
        if stock[name] < count:
            rejected.append(f"{i + 1}|{name}|{count}|{stock[name]}")
        else:
            stock[name] -= count

f = open("stock_final.txt", "w", encoding="utf-8")
for name in sorted(stock.keys()):
    if stock[name] > 0:
        f.write(f"{name}|{stock[name]}\n")
f.close()

f = open("rejected.txt", "w", encoding="utf-8")
for r in rejected:
    f.write(r + "\n")
f.close()

#10

fa = open("server_a.txt", encoding="utf-8")
fb = open("server_b.txt", encoding="utf-8")
out = open("timeline.txt", "w", encoding="utf-8")

line_a = fa.readline()
line_b = fb.readline()

while line_a != "" or line_b != "":
    if line_a == "":
        out.write(line_b)
        line_b = fb.readline()
    elif line_b == "":
        out.write(line_a)
        line_a = fa.readline()
    else:
        if line_a[:8] <= line_b[:8]:
            out.write(line_a)
            line_a = fa.readline()
        else:
            out.write(line_b)
            line_b = fb.readline()

fa.close()
fb.close()
out.close()