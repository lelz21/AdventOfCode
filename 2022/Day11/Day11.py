from collections import deque
from multiprocessing import synchronize
from typing import Tuple

neighbors = [
    (-1, 0), (1, 0), (0, -1), (0, 1), 
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

def checkBounds(coords: Tuple[int, int], bounds: Tuple[int, int]) -> bool:
    return coords[0] >= 0 and coords[0] < bounds[0] and coords[1] >= 0 and coords[1] < bounds[1]

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    grid = [[int(c) for c in line.replace('\n', '')] for line in file.readlines()]

    m = len(grid)
    n = len(grid[0])
    size = m * n
    flashes = 0
    synchronizing = 0
    iterations = 0
    # for counter in range(100):
    while synchronizing < size:
        #Step 1:
        v = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    q.append((i, j))
                    v.add((i, j))
        
        #Step 2:
        while len(q):
            i, j = q.pop()
            for nx, ny in neighbors:
                if checkBounds((i + nx, j + ny), (m, n)):
                    grid[i + nx][j + ny] += 1
                    if grid[i + nx][j + ny] > 9 and (i + nx, j + ny) not in v:
                        q.append((i + nx, j + ny))
                        v.add((i + nx, j + ny))
        
        #Step 3:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 9:
                    grid[i][j] = 0
        synchronizing = len(v)
        if (iterations < 100):
            flashes += synchronizing
        iterations += 1
    
    print(flashes, iterations)

def main() -> None:
    exec("Day11/Day11.txt")

if __name__ == "__main__":
    main()