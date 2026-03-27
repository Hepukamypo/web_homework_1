n = int(input())

A = []
B = []

for _ in range(n):
    A.append(list(map(int, input().split())))

for _ in range(n):
    B.append(list(map(int, input().split())))

result = []

for i in range(n):
    row = []
    for j in range(n):
        s = 0
        for k in range(n):
            s += A[i][k] * B[k][j]
        row.append(s)
    result.append(row)

for row in result:
    print(*row)         