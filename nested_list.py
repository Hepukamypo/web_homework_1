dct = dict()
scores = set()

for _ in range(int(input())):
	name=input()
	score=float(input())
	scores.add(score)
	dct.setdefault(score, list())
	dct[score].append(name)

scores = sorted(list(scores))
students = sorted(dct[scores[1]])
for student in students:
	print(student)