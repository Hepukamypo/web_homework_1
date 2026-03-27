s1 = input()
dct1 = dict()
for l in sorted(list(set(s1))):
	dct1[l] = s1.count(l)

s2 = input()
dct2 = dict()
for l in sorted(list(set(s2))):
	dct2[l] = s2.count(l)

print('YES' if dct1==dct2 else 'NO')