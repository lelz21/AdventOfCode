import numpy as np
neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def make5x5(mat: np.matrix) -> np.matrix:
    offset = np.arange(5)
    offset = offset[:,None] + offset
    offset = np.repeat(offset, mat.shape[0], axis = 0)
    offset = np.repeat(offset, mat.shape[1], axis = 1)
    # print(offset)

    mat = np.tile(mat, [5, 5])
    # print(mat.shape)

    rows, cols = mat.shape
    for y in range(rows):
            for x in range(cols):
                mat[y][x] += offset[y][x]
                if mat[y][x] > 9:
                    mat[y][x] -= 9
    # print(mat)
    return mat

def exec(fileName: str) -> None:
    
    mat = np.loadtxt(fileName, int)
    # mat = make5x5(mat)
    # visited = np.zeros(mat.shape)
    TDV = np.ones(mat.shape, int) * np.inf
    TDV[0][0] = 0

    idx = np.indices(mat.shape)
    nVisited = set()
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            nVisited.add((idx[0][i][j], idx[1][i][j]))
    
    rows, cols = mat.shape
    cy, cx = 0, 0
    while cy != rows - 1 or cx != cols - 1:
        for nx, ny in neighbours:
            ny, nx = ny + cy, nx + cx
            if ny >= 0 and ny < rows and nx >= 0 and nx < cols and (ny, nx) in nVisited:
                TDV[ny][nx] = min(TDV[ny][nx], TDV[cy][cx] + mat[ny][nx])

        nVisited.discard((cy, cx))
        minTDV = np.inf
        for y, x in nVisited:
            if minTDV > TDV[y][x]:
                minTDV = TDV[y][x]
                cy, cx = y, x
    print(TDV[rows - 1][cols - 1])

def main() -> None:
    exec("Day15/Day15.txt")

if __name__ == "__main__":
    main()