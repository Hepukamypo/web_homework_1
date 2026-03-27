s=input()
vowels = 'AEIOUY'
kevin=0
stuart=0
for start in range(len(s)):
	for end in range(start, len(s)):
		w = s[start:end+1]
		if w[0] in vowels:
			kevin+=1
		else:
			stuart+=1

print(f'{'Стюарт' if stuart > kevin else 'Кевин'} {max(stuart, kevin)}')