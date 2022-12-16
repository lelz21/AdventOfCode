def visibilityAndScore(y: int, x: int, grid :list) -> tuple:

    current = grid[y][x]
    
    inc = 1
    visibilty = {
        "North" : True, 
        "South" : True, 
        "East" : True, 
        "West" : True
    }

    score = {
        "North" : 0, 
        "South" : 0, 
        "East" : 0, 
        "West" : 0
    }
    
    while y - inc >= 0 or y + inc < len(grid) or x - inc >= 0 or x + inc < len(grid[y]):

        if y - inc >= 0 and visibilty["North"] == True:
            score["North"] += 1
            if  grid[y - inc][x] >= current:
                visibilty["North"] = False

        if y + inc < len(grid) and visibilty["South"] == True:
            score["South"] += 1
            if  grid[y + inc][x] >= current:
                visibilty["South"] = False


        if x - inc >= 0 and visibilty["East"] == True:
            score["East"] += 1
            if grid[y][x - inc] >= current:
                visibilty["East"] = False

        if x + inc < len(grid[y]) and visibilty["West"] == True:
            score["West"] += 1
            if grid[y][x + inc] >= current:
                visibilty["West"] = False
        inc += 1
    
    finalVisibility = 1 if visibilty["North"] or visibilty["South"] or visibilty["East"] or visibilty["West"] else 0
    finalScore = score["North"] * score["South"] * score["East"] * score["West"]
    
    return finalVisibility, finalScore


def exec(fileName: str) -> None:

    file = open(fileName, "r")

    grid = [[int(c) for c in line.replace('\n', '')] for line in file.readlines()]

    count = 0
    bestScore = 0

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            visibility, score  = visibilityAndScore(y, x, grid)
            count += visibility
            bestScore = max(score, bestScore)

    print(count + (len(grid) * 2 + len(grid[0]) * 2 - 4), bestScore)


def main() -> None:
    exec("2023/Day08/Day08.txt")

if __name__ == "__main__":
    main()