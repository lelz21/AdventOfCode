from typing import List, Tuple

class Board:
    
    def __init__(self, size: Tuple[int], lines: List[List[str]]) -> None:
        self.size = size
        self.fromTo = [range(self.size[0]), range(self.size[1])]
        self.content = [[0, False] * self.size[1]] * self.size[0]
        self.won = False

        for j in range(6):
            self.addLine(j - 1, lines[j])

    def addLine(self, i: int, line: List[str]) ->None:
        line = line.replace("\n", "")
        if len(line) > 0:
            self.content[i] = [[int(n), False] for n in line.split()]
    
    def at(self, i: int, j: int) -> Tuple[int, bool]:
        if i < self.size[0] and j < self.size[1]:
            return self.content[i][j]

    def check(self, num: int) -> bool:
        for i in self.fromTo[0]:
            for j in self.fromTo[1]:
                if self.content[i][j][0] == num:
                    self.content[i][j][1] = True

        self.won = self.checkDim(0) or self.checkDim(1)
        return self.won

    def checkDim(self, dim: int) -> bool:
        for i in self.fromTo[dim]:
            b = True
            for j in self.fromTo[not dim]:
                b = b and self.content[i if dim else j][j if dim else i][1]
            if b == True:
                return True
        return False

    def uncheckedSum(self) -> int:
        return sum([item for sublist in [[elem[0] for elem in row if elem[1] == False] for row in self.content] for item in sublist])

    def __repr__(self) -> str:
        s = "["
        for i in self.fromTo[0]:
            s += "["
            for j in self.fromTo[1]:
                s += str(self.content[i][j])
                s += ", " if j != self.size[1] - 1 else ""
            s += "]\n " if i != self.size[0] - 1 else "]"
        s += "]\n"
        return s
    
    def __str__(self) -> str:
        s = "["
        for i in self.fromTo[0]:
            s += "["
            for j in self.fromTo[1]:
                s += str(self.content[i][j])
                s += ", " if j != self.size[1] - 1 else ""
            s += "]\n " if i != self.size[0] - 1 else "]"
        s += "]\n"
        return s