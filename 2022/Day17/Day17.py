import math

def isIn(target: tuple, pos: tuple) -> bool:
    return pos[0] >= target[0] and pos[0] <= target[2] and pos[1] >= target[1] and pos[1] <= target[3]

def throwProbe(target: tuple, v: tuple, minY: int, pos: tuple = (0, 0)) -> bool:

    while pos[1] >= minY and not isIn(target, pos):
        pos = (pos[0] + v[0], pos[1] + v[1])
        if v[0] > 0:
            v = (v[0] - 1, v[1] - 1)
        elif v[0] < 0:
            v = (v[0] + 1, v[1] - 1)
        else:
            v = (v[0], v[1] - 1)

    return isIn(target, pos)

def minXVelocity(x: int) -> int:
    r = 0
    c = 0
    while r < x:
        r += c
        c += 1
    return c - 1

def exec(fileName: str) -> None:
    file = open(fileName, "r")
    
    _, _, x, y = file.readline().split()
    x = [int(a) for a in x[2:-1].split("..")]
    y = [int(a) for a in y[2:].split("..")]

    maxHeight = math.comb(abs(y[0]), 2)
    print(maxHeight)

    counter = 0
    for i in range(minXVelocity(x[0]), x[1] + 1):
        for j in range(y[0], abs(y[0])):
            if throwProbe((x[0], y[0], x[1], y[1]), (i, j), y[0]):
                counter += 1

    print(counter)

def main() -> None:
    exec("Day17/Day17.txt")

if __name__ == "__main__":
    main()