n, m = map(int, input().split()) # грузоподъёмность, кол-во грузов
cost_dct = dict() # словарь {ценность:[груз1, груз2 ...]}
dct = dict() # словарь {груз: [вес, стоимость]}
for _ in range(m):
	cargo = input().split() # создаём список [название, вес, цена]
	cost_dct.setdefault(int(cargo[2]) / int(cargo[1]), []) # добаляем ценность как ключ в словарь и по умолчанию ставим пустой список значением
	cost_dct[int(cargo[2]) / int(cargo[1])].append(cargo[0]) # добавляем в список ключа ценности название груза
	dct[cargo[0]] = [int(cargo[1]), int(cargo[2])]

for k in sorted(cost_dct.keys(), reverse=True): # проходимся по самым ценным грузам
	values = cost_dct[k]
	for item in values:
		if n > dct[item][0]: # если оставшаяся грузоподъёмность больше веса груза
			print(f'{item} {dct[item][0]} {dct[item][1]}')
			n -= dct[item][0]
		elif n == dct[item][0]: # если оставшаяся грузоподъёмность равна весу груза
			print(f'{item} {dct[item][0]} {dct[item][1]}') 
			exit()
		elif n < dct[item][0]: # если оставшаяся грузоподъёмность меньше веса груза
			print(f'{item} {n} {(dct[item][1] * (n / dct[item][0])):.2f}')
			exit()