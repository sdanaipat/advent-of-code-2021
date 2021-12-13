from collections import defaultdict

def input():
    with open("input.txt") as f:
        bingo_seq = f.readline().strip().split(",")
        bingo_seq = [int(num) for num in bingo_seq]
        next(f)
        bingo_boards = []
        board = []
        for line in f:
            line = line.strip()
            if not line:
                bingo_boards.append(board)
                board = []
            else:
                board.append([int(num) for num in line.split()])
        return bingo_seq, bingo_boards


class BingoBoard:
    def __init__(self, i, board_array, global_idx):
        self.i = i
        self.sum = 0
        self.rows = [0] * 5
        self.cols = [0] * 5
        self.idx = {}
        for i, row in enumerate(board_array):
            for j, num in enumerate(row):
                self.idx[num] = (i, j)
                global_idx[num].append(self)
                self.sum += num

    def is_bingo(self):
        return any(row == 5 for row in self.rows) or \
            any(col == 5 for col in self.cols)


    def mark(self, num):
        i, j = self.idx[num]
        self.rows[i] += 1
        self.cols[j] += 1
        self.sum -= num


def solve1():
    seq, boards = input()
    global_idx = defaultdict(list)
    boards = [BingoBoard(i, b, global_idx) for i, b in enumerate(boards)]
    
    done = set()
    won_last = None
    for num in seq:
        for board in global_idx[num]:
            if board.i in done:
                continue
            board.mark(num)
            if board.is_bingo():
                won_last = num * board.sum
                done.add(board.i)
    return won_last





