

def input():
    with open("input.txt") as f:
        for line in f:
            cmd, val = line.strip().split()
            yield cmd, int(val)


def solve1():
    x = 0
    y = 0
    for cmd, val in input():
        if cmd == "forward":
            x += val
        elif cmd == "up":
            y -= val
        else:
            y += val
    return x, y, x * y


def solve2():
    x = y = 0
    aim = 0
    for cmd, val in input():
        if cmd == "forward":
            x += val
            y += val * aim
        elif cmd == "up":
            aim -= val
        else:
            aim += val
    return x, y, x * y

print(solve1())
print(solve2())
