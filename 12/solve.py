from collections import defaultdict 
from collections import Counter


def input():
    with open("input.txt") as f:
        inp = ""
        for line in f:
            inp += line
        return inp

test1_res1 = 10
test2_res1 = 36
test_inp1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

test1_res2 = 19
test2_res2 = 103
test_inp2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

test1_res3 = 226
test2_res3 = 3509
test_inp3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def build_graph(inp):
    G = defaultdict(list)
    for line in inp.split("\n"):
        if not line:
            continue
        a, b = line.split("-")
        G[a].append(b)
        G[b].append(a)
    return G


def test_solve1():
    assert test1_res1 == solve1(test_inp1)
    assert test1_res2 == solve1(test_inp2)
    assert test1_res3 == solve1(test_inp3)


def test_solve2():
    assert test2_res1 == solve2(test_inp1)
    assert test2_res2 == solve2(test_inp2)
    assert test2_res3 == solve2(test_inp3)


def solve1(inp):
    def backtrack(u, visited, visited_path, G):
        if u.islower() and u in visited:
            return 0
        k = (u, frozenset(visited))
        if k in visited_path:
            return 0
        if u == "end":
            return 1
        ans = 0
        visited.add(u)
        visited_path.add(k)
        for v in G[u]:
            ans += backtrack(v, visited, visited_path, G)
        if u in visited:
            visited.remove(u)
        if k in visited_path:
            visited_path.remove(k)
        return ans

    G = build_graph(inp)
    return backtrack("start", set(), set(), G)


def solve2(inp):
    
    def can_visit(u, visited, visited_path):
        if u == "start":
            return u not in visited
        if u.isupper():
            return True
        repeated_small = any(n > 1 for v, n in visited.items() if v.islower())
        if visited[u] > 0 and repeated_small:
            return False
        k = (u, frozenset(v for v, n in visited.items() if n))
        if k in visited_path:
            return False
        return True

    def backtrack(u, visited, visited_path, G):
        if not can_visit(u, visited, visited_path):
            return 0
        if u == "end":
            return 1
        ans = 0
        k = (u, frozenset(v for v, n in visited.items() if n))
        visited[u] += 1
        visited_path.add(k)
        for v in G[u]:
            ans += backtrack(v, visited, visited_path, G)
        visited[u] -= 1
        visited[u] = max(0, visited[u])
        if k in visited_path:
            visited_path.remove(k)
        return ans
    
    G = build_graph(inp)
    return backtrack("start", Counter(), set(), G)

                

