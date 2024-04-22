# Matrix size
s = int(input())
matrix = []

# User input
for _ in range(s):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

# Result
for a in range(s):
    for b in range(s - 1, -1, -1):
        print(matrix[b][a], end=' ')
    print()
