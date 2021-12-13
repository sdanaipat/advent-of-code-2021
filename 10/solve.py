


def input():
    with open("input.txt") as f:
        for line in f:
            yield line.strip()

OPEN = set("<[({")
CLOSE = set(">])}")


def get_score(inp):
    """
    >>> get_score("}}]])})]")
    288957
    """
    ans = 0
    for c in inp:
        ans *= 5
        if c == ")":
            ans += 1
        elif c == "]":
            ans += 2
        elif c == "}":
            ans += 3
        else:
            ans += 4
    return ans


def complete_brackets(inp):
    """
    >>> complete_brackets("[({(<(())[]>[[{[]{<()<>>")
    '}}]])})]'
    """
    S = []
    for c in inp:
        if c in OPEN:
            S.append(c)
        else:
            S.pop()
    ans = ""
    while S:
        c = S.pop()
        if c == "(":
            ans += ")"
        elif c == "[":
            ans += "]"
        elif c == "{":
            ans += "}"
        else:
            ans += ">"
    return ans


def solve2():
    scores = []
    for inp in input():
        if compute_err(inp) > 0:
            continue
        b = complete_brackets(inp)
        scores.append(get_score(b))
    scores.sort()
    m = len(scores) // 2
    return scores[m]



def compute_err(inp):
    S = []
    ans = 0
    for c in inp:
        if c in OPEN:
            S.append(c)
        elif S:
            o = S.pop()
            if c == ")" and o != "(":
                ans += 3
            elif c == "]" and o != "[":
                ans += 57
            elif c == "}" and o != "{":
                ans += 1197
            elif c == ">" and o != "<":
                ans += 25137
        else:
            # incomplete
            return 0
    return ans


def solve1():
    ans = 0
    for inp in input():
        ans += compute_err(inp)
    return ans

