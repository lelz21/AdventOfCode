import sys
from typing import List, Set, Tuple

neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def keepMax(l: List[int], n: int) -> None:
    if l[0] < n:
        if l[1] < n:
            if l[2] < n:
                l[0], l[1], l[2] = l[1], l[2], n
            else:
                l[0], l[1] = l[1], n
        else:
            l[0] = n


def dfs(field: List[str], i: int, j: int, C: int, R: int, visited: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    
    visited.add((i, j))
    
    for nx, ny in neighbors:
        if i + nx >= 0 and i + nx < C and j + ny >= 0 and j + ny < R:
            if int(field[i][j]) < int(field[i + nx][j + ny]) and int(field[i + nx][j + ny]) < 9 :
                if (i + nx, j + ny) not in visited:
                    visited.union(dfs(field, i + nx, j + ny, C, R, visited))
    return visited

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    field = []
    for line in file.readlines():
        field.append(line.strip())
        
    C = len(field)
    R = len(field[0])
    s = 0
    largest = [0, 0, 0]
    for i in range(C):
        for j in range(R):
            b = True
            for nx, ny in neighbors:
                if i + nx >= 0 and i + nx < C and j + ny >= 0 and j + ny < R and int(field[i][j]) >= int(field[i + nx][j + ny]):
                    b = False
            if b == True:
                keepMax(largest, len(dfs(field, i, j, C, R, set())))
                s += int(field[i][j]) + 1
    print(s)
    print(largest[0] * largest[1] * largest[2])

def main() -> None:
    exec("Day09/Day09.txt")

if __name__ == "__main__":
    main()