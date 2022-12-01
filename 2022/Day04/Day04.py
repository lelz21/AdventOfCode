
from Board import Board

def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    numbers = [int(n) for n in file.readline().split(",")]

    boards = []
    boardLines = file.readlines()
    nbBoards = int(len(boardLines) / 6)
    for i in range(nbBoards):
        board = Board((5, 5), boardLines[i * 6:(i + 1) * 6])
        boards.append(board)

    #Boards of interest
    BOI = [0, 0]
    i = 0
    j = 0
    while i < len(numbers) and j < nbBoards:
        for board in boards:
            if not board.won and board.check(numbers[i]):
                if j == 0:
                    BOI[0] = numbers[i] * board.uncheckedSum()
                elif j == nbBoards - 1:
                    BOI[1] = numbers[i] * board.uncheckedSum()
                else:
                    pass
                j += 1
        i += 1

    print(BOI)

def main() -> None:
    exec("Day04/Day04.txt")

if __name__ == "__main__":
    main()