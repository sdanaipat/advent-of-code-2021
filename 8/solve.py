from collections import defaultdict


def input():
    with open("input.txt") as f:
        for line in f:
            head, tail = line.strip().split(" | ")
            head = head.split()
            tail = tail.split()
            yield head, tail


def backtrack(H, picked, solution, heads):
    if len(solution) == 7:
        return solution
    cur = chr(len(solution) + ord("a"))
    candidates = H[cur] - picked
    if not candidates:
        return None
    
    for c in candidates:
        solution[cur] = c
        picked.add(c)
        s = backtrack(H, picked, solution, heads)
        if s and valid(s, heads):
            return s
        picked.remove(c)
        del solution[cur]


def valid(mapping, heads):
    nums = set(range(10))
    try:
        for h in heads:
            num = to_num(h, mapping)
            nums.remove(num)
    except KeyError:
        return False
    return not nums



def to_num(signal, mapping):
    inv_on = {
            frozenset("abcefg"): 0,
            frozenset("cf"): 1,
            frozenset("acdeg"): 2,
            frozenset("acdfg"): 3,
            frozenset("bcdf"): 4,
            frozenset("abdfg"): 5,
            frozenset("abdefg"): 6,
            frozenset("acf"): 7,
            frozenset("abcdefg"): 8,
            frozenset("abcdfg"): 9,
    }

    s = frozenset(mapping[s] for s in signal)
    return inv_on[s]


def solve2():
    on = {
        0: set("abcefg"),
        1: set("cf"),
        2: set("acdeg"),
        3: set("acdfg"),
        4: set("bcdf"),
        5: set("abdfg"),
        6: set("abdefg"),
        7: set("acf"),
        8: set("abcdefg"),
        9: set("abcdfg"),
    }
    off = {idx: set("abcdefg") - val for idx, val in on.items()}
    
    easy = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }
    H = {
        "a": set("abcdefg"),
        "b": set("abcdefg"),
        "c": set("abcdefg"),
        "d": set("abcdefg"),
        "e": set("abcdefg"),
        "f": set("abcdefg"),
        "g": set("abcdefg"),
    }
    ans = 0
    for head, tail in input():
        for display in head:
            if len(display) in easy:
                val = easy[len(display)]
                for s in display:
                    H[s] |= on[val]
                    H[s] -= off[val]
        mapping = backtrack(H, set(), {}, head)
        val = 0
        for digit in tail:
            val = val * 10 + to_num(digit, mapping)
        print(val)
        ans += val
    return ans


def solve1():
    ans = 0
    for _, tail in input():
        for x in tail:
            if len(x) in {2, 3, 4, 7}:
                ans += 1
    return ans
