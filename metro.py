l = list()
counter = 0
for _ in range(int(input())):
	l.append(list(map(int, input().split())))
t = int(input())
for e in l:
	if e[0]<= t and e[1] >= t:
		counter +=1

print(counter)