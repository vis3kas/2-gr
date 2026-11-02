market = {"молоко": 20, "сыр": 15, "шоколадка": 50}
market2 = {"мороженное": 40, "сыр": 20, "молоко": 5, "шоколадка": 50}

out = {}

for i in market.keys() | market2.keys():
    out[i] = market.get(i, 0) + market2.get(i, 0)

print(out)