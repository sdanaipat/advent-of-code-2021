from collections import deque


def solve1():
    ans = 0
    prev = float("inf")
    with open("input.txt") as f:
        for line in f:
            d = int(line.strip())
            ans += 1 if d > prev else 0
            prev = d
    print(ans)


def solve2():
    ans = 0
    w = deque()
    s = 0
    prev = float("inf")
    with open("input.txt") as f:
        for line in f:
            d = int(line.strip())
            s += d
            w.append(d)
            if len(w) > 3:
                s -= w.popleft()
            print(d, len(w), s)
            if len(w) == 3:
                if s > prev:
                    ans += 1
                prev = s
    print(ans)


if __name__ == "__main__":
    # solve1()
    solve2()
