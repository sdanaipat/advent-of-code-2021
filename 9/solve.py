import numpy as np


def input():
    with open("input.txt") as f:
        A = []
        for line in f:
            line = line.strip()
            row = list(map(int, list(line)))
            A.append(row)
        return np.array(A, dtype=int)


def low_point(M, i, j):
    x = M[i, j]
    if i - 1 >= 0 and x >= M[i-1, j]:
        return False
    if i + 1 < M.shape[0] and x >= M[i+1, j]:
        return False
    if j - 1 >= 0 and x >= M[i, j-1]:
        return False
    if j + 1 < M.shape[1] and x >= M[i, j + 1]:
        return False
    return True


def basin_size(M, i, j):

    def dfs(x, y, visited):
        if (x, y) in visited:
            return 0
        if x < 0 or y < 0 or x >= M.shape[0] or y >= M.shape[1]:
            return 0
        if M[x, y] == 9:
            return 0
        visited.add((x, y))
        return 1 + dfs(x-1, y, visited) + \
            dfs(x+1, y, visited) + \
            dfs(x, y-1, visited) + \
            dfs(x, y+1, visited)
    return dfs(i, j, set())

def solve2():
    M = input()
    m, n = M.shape
    sizes = []
    for i in range(m):
        for j in range(n):
            if low_point(M, i, j):
                s = basin_size(M, i, j)
                sizes.append(s)
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def solve1():
    M = input()
    m, n = M.shape 
    low_points = []
    for i in range(m):
        for j in range(n):
            if low_point(M, i, j):
                low_points.append(M[i, j] + 1)
    return sum(low_points)
