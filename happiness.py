n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for e in arr:
	if e in A:
		happiness+=1
	elif e in B:
		happiness-=1

print(happiness)