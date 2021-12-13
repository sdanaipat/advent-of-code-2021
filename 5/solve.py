from collections import namedtuple, Counter


class Point(namedtuple("Point", "x y")):
    ...
    
class Line(namedtuple("Line", "p q")):

    def is_vertical(self):
        return self.p.x == self.q.x

    def is_horizontal(self):
        return self.p.y == self.q.y

    def is_diag(self):
        return abs(self.p.x - self.q.x) == abs(self.p.y - self.q.y)


def input():
    with open("input.txt") as f:
        for line in f:
            a, b = line.strip().split(" -> ")
            a = list(map(int, a.split(",")))
            b = list(map(int, b.split(",")))
            a = Point(*a)
            b = Point(*b)
            yield Line(a, b)


def solve1():
    """
    """

    ans = Counter()
    for l in input():
        if l.is_vertical():
            start = min(l.p.y, l.q.y)
            end = max(l.p.y, l.q.y)
            for y in range(start, end + 1):
                ans[(l.p.x, y)] += 1
        elif l.is_horizontal():
            start = min(l.p.x, l.q.x)
            end = max(l.p.x, l.q.x)
            for x in range(start, end + 1):
                ans[(x, l.p.y)] += 1
        elif l.is_diag():
            x = l.p.x
            y = l.p.y
            ans[(x, y)] += 1
            while x != l.q.x and y != l.q.y:
                x += 1 if x < l.q.x else -1
                y += 1 if y < l.q.y else -1
                ans[(x, y)] += 1


    return len(list(v for v in ans.values() if v > 1))
