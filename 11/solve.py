import numpy as np
from scipy.signal import convolve2d


def input():
    X = np.empty((10, 10), dtype=np.int)
    with open("input.txt") as f:
        for i, line in enumerate(f):
            row = np.array(list(map(int, list(line.strip()))))
            X[i] = row
    return X


def step(X):
    X += 1
    flash = (X > 9).astype(np.int)
    n = flash.sum()
    flashed = flash == 1
    ans = 0
    while n > 0:
        ans += n
        w = np.ones((3, 3))
        X += (convolve2d(flash, w, mode="same") - flash).astype(np.int)
        X[flashed] = 0
        
        flash = (X > 9).astype(np.int)
        n = flash.sum()
        flashed |= flash == 1

    return ans


def solve1():
    N = 100
    ans = 0
    X = input()
    for _ in range(N):
        ans += step(X)
    return ans


def solve2():
    X = input()
    ans = 0
    while X.sum():
        step(X)
        ans += 1
    return ans
