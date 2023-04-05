from collections import deque
import sys
sys.stdin = open('5427.txt', 'r')
input = sys.stdin.readline


def fire(ti, tj):
    for mi, mj in direction:
        fi, fj = ti + mi, tj + mj
        if 0 <= fi < h and 0 <= fj < w and building[fi][fj] != '#' and building[fi][fj] != '*':
            if building[fi][fj] != '&':
                building[fi][fj] = '&'


def bfs(si, sj):
    visited = [([0] * w) for _ in range(h)]
    queue = deque()
    queue.append((si, sj, 1))
    visited[si][sj] = 1
    check = 1

    while queue:
        ci, cj, cc = queue.popleft()
        if cc == check + 1:
            for a in range(h):
                for b in range(w):
                    if building[a][b] == '*':
                        fire(a, b)
            for x in range(h):
                for y in range(w):
                    if building[x][y] == '&':
                        building[x][y] = '*'
            check = cc
        for mi, mj in direction:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < h and 0 <= nj < w and (visited[ni][nj] == 0) and (building[ni][nj] == '.'):
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni, nj, visited[ni][nj]))
                building[ni][nj] = '@'
            if ni < 0 or nj < 0 or ni >= h or nj >= w:
                return visited[ci][cj]


Test_case = int(input())

for t in range(Test_case):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                start_i, start_j = i, j
    result = 'IMPOSSIBLE'
    temp = bfs(start_i, start_j)
    if temp:
        result = temp

    print(result)
