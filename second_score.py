n=int(input())
A = sorted(list(set(map(int, input().split()))), reverse=True)
print(A[1])