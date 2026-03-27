n, m = map(int, input().split()) # грузоподъёмность, кол-во грузов
cost_dct = dict() # словарь ценность:список грузов
dct = dict() # словарь груз:вес и стоимость
for _ in range(m):
	cargo = input().split()
	cost_dct.setdefault(int(cargo[2]) / int(cargo[1]), [])
	cost_dct[int(cargo[2]) / int(cargo[1])].append(cargo[0])
	dct[cargo[0]] = [int(cargo[1]), int(cargo[2])]

for k in sorted(cost_dct.keys(), reverse=True):
	values = cost_dct[k]
	for item in values:
		if n > dct[item][0]:
			print(f'{item} {dct[item][0]} {dct[item][1]}')
			n -= dct[item][0]
		elif n == dct[item][0]:
			print(f'{item} {dct[item][0]} {dct[item][1]}')
			exit()
		elif n < dct[item][0]:
			print(f'{item} {n} {(dct[item][1] * (n / dct[item][0])):.2f}')
			exit()