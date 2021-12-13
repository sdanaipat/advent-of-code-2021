

def input():
    with open("input.txt") as f:
        for line in f:
            yield line.strip()


from collections import Counter

def solve1():
    bits = Counter()
    for val in input():
        k = len(val)
        print(k)
        for i in range(k):
            if val[i] == "1":
                bits[i] += 1
            else:
                bits[i] -= 1
    print([bits[i] for i in range(k)])
    gamma = int("".join("1" if bits[i] > 0 else "0" for i in range(k)), 2)
    eps = gamma ^ ((1 << k) - 1)
    ans = gamma * eps

    return f"{gamma:b} {eps:b}", ans


def solve2():
    def find_o2(vals, i=0):
        if len(vals) == 1:
            return vals.pop()
        ones = []
        zeros = []
        for val in vals:
            if val[i] == "1":
                ones.append(val)
            else:
                zeros.append(val)
        if len(ones) >= len(zeros):
            return find_o2(ones, i + 1)
        else:
            return find_o2(zeros, i + 1)
    
    def find_co2(vals, i=0):
        if len(vals) == 1:
            return vals.pop()
        ones = []
        zeros = []
        for val in vals:
            if val[i] == "1":
                ones.append(val)
            else:
                zeros.append(val)
        if len(ones) < len(zeros):
            return find_co2(ones, i + 1)
        else:
            return find_co2(zeros, i + 1)
    
    inp = list(input())
    o2 = find_o2(inp)
    co2 = find_co2(inp)
    
    print(o2, co2)
    return int(o2, 2) * int(co2, 2)

print(solve2())
