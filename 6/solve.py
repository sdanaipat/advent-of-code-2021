from collections import namedtuple
from collections import Counter


def input():
    with open("input.txt") as f:
        line = f.readline()
        return list(map(int, line.strip().split(",")))
    

def fish(t):
    while True:
        if t == 0:
            t = 6
        else:
            t -= 1
        yield t
               
def solve(days):
    F = Counter(input())
    for _ in range(days):
        G = Counter()
        for t, n in F.items():
            if t == 0:
                G[8] += n
            t = next(fish(t))
            G[t] += n
        F = G
    return sum(n for n in F.values())
    

def solve1():
    """
    >>> solve1()
    361169
    """
    return solve(80)


def solve2():
    return solve(256)
            
