import numpy as np
from scipy.sparse import coo_matrix

def input(input_fname="input.txt"):
    with open(input_fname) as f:
        X = []
        Y = []
        for line in f:
            if not line.strip():
                break
            i, j = line.strip().split(",")
            X.append(int(i))
            Y.append(int(j))
        data = np.ones(len(X))
        paper = coo_matrix((data, (Y, X)))
        
        #read commands
        cmds = []
        for line in f:
            axis, idx = line.strip().split(" ")[-1].split("=")
            cmds.append((axis, int(idx)))
        
        return paper, cmds


def test_input():
    return input("test_input.txt")


def test_solve1():
    paper, cmds = test_input()
    assert solve1(paper, cmds[:1]) == 17


def fold_along_y(paper, y):
    top = paper.tocsr()[:y]
    bottom = paper.tocsr()[y+1:]
    folded = top + bottom[::-1]
    folded[folded > 0] = 1
    return folded


def fold_along_x(paper, x):
    return fold_along_y(paper.T, y=x).T


def solve1(paper, cmds):
    axis, idx = cmds[0]
    if axis == "y":
        return fold_along_y(paper, idx).sum()
    else:
        return fold_along_x(paper, idx).sum()


def solve2(paper, cmds):
    
    def print_paper(paper):
        for row in paper.todense():
            print("".join("*" if x else " " for x in np.array(row)[0]))

    for axis, idx in cmds:
        if axis == "y":
            paper = fold_along_y(paper, idx)
        else:
            paper = fold_along_x(paper, idx)
    print_paper(paper)
