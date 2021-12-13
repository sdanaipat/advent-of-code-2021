import numpy as np
from scipy.optimize import minimize


def input():
    with open("input.txt") as f:
        line = f.readline()
        return list(map(int, line.strip().split(",")))

def init_cost_func(positions):
    def cost(x):
        return np.abs(positions - x).sum()
    return cost
    

def init_cost_func2(positions):
    def cost(x):
        d = np.abs(positions - x)
        return (d * (d + 1) // 2).sum()
    return cost

def solve1():
    """
    >>> solve1()
    355150
    """
    positions = np.array(input())
    cost = init_cost_func(positions)
    solution = minimize(cost, np.mean(input()))
    a = np.ceil(solution.x[0])
    b = np.floor(solution.x[0])

    return int(min(cost(a), cost(b)))


def solve2():
    positions = np.array(input())
    cost = init_cost_func2(positions)
    solution = minimize(cost, np.mean(input()))
    a = np.ceil(solution.x[0])
    b = np.floor(solution.x[0])

    return int(min(cost(a), cost(b)))

