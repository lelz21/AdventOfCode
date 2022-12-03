mapSelectedScore = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

mapTranslatedScore = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

def mapNeedToEnd(opp: chr, out: chr) -> chr:
    if out == "Y":
        return chr(ord(opp) + 23)
    elif out == "X":
        if opp == "A" : return "Z"
        elif opp == "B" : return "X"
        else : return "Y"
    else:
        if opp == "A" : return "Y"
        elif opp == "B" : return "Z"
        else : return "X"

def outcomeScore(opp: chr, you: chr) -> int:
    if chr(ord(opp) + 23) == you:
        return 3
    elif opp == "A":
        return 6 if you == "Y" else 0
    elif opp == "B":
        return 6 if you == "Z" else 0
    else:
        return 6 if you == "X" else 0


def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    
    sumPart1 = 0
    sumPart2 = 0

    for line in file.readlines():
        in1, in2 = line.replace("\n", "").split(" ")
        sumPart1 += mapSelectedScore[in2] + outcomeScore(in1, in2)
        
        selected = mapNeedToEnd(in1, in2)
        sumPart2 += mapSelectedScore[selected] + mapTranslatedScore[in2]
        
    print(sumPart1, sumPart2)

def main() -> None:
    exec("2023/Day02/Day02.txt")

if __name__ == "__main__":
    main()