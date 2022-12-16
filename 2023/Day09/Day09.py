import math

motions = {
    "L" : [-1, 0],
    "R" : [1, 0],
    "U" : [0, 1],
    "D" : [0, -1]
}

def keepUp(head: list, tail: list) -> None:
    for coord in range(2):
        if head[coord] > tail[coord]:
            tail[coord] += 1
        elif head[coord] < tail[coord]:
            tail[coord] -= 1

def exec(fileName: str) -> None:

    file = open(fileName, "r")

    #Part 1
    head = [0, 0]
    tail = [0, 0]
    visitedPart1 = set()

    #Part 2
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visitedPart2 = set()
    for line in file.readlines():
        direction, steps = line.replace("\n", "").split()

        vec = motions[direction]
        for i in range(int(steps)):
            #Part 1
            head = [head[0] + vec[0], head[1] + vec[1]]
            dist = math.sqrt(pow(head[0] - tail[0], 2) + pow(head[1] - tail[1], 2))
            if dist > math.sqrt(2):
                keepUp(head, tail)
            visitedPart1.add(tuple(tail))

            #Part 2
            rope[0] = [rope[0][0] + vec[0], rope[0][1] + vec[1]]
            for knot in range(1, len(rope)):
                dist = math.sqrt(pow(rope[knot - 1][0] - rope[knot][0], 2) + pow(rope[knot - 1][1] - rope[knot][1], 2))
                if dist > math.sqrt(2):
                    keepUp(rope[knot - 1], rope[knot])
            visitedPart2.add(tuple(rope[9]))

    print(len(visitedPart1))
    print(len(visitedPart2))

def main() -> None:
    exec("2023/Day09/Day09.txt")

if __name__ == "__main__":
    main()