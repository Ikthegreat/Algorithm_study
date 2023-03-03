paper = [[0] * 101 for _ in range(101)]
for _ in range(4):
    X1, Y1, X2, Y2 = map(int, input().split())

    for i in range(X1, X2):
        for j in range(Y1, Y2):
            paper[i][j] = 1

count = 0
for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            count += 1

print(count)
