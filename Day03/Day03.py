from typing import List

def nbOnesFromCol(l: List[str], col: int)  -> int:
    i = 0
    for line in l:
        i += int(line[col])
    return i

def nbOnesPerCol(l: List[str], lineSize: int) -> List[int]:
    nbOnes = [0] * lineSize
    for i in range(lineSize):
            nbOnes[i] = nbOnesFromCol(l, i)
    return nbOnes

def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    lines = file.readlines()

    lineSize = len(lines[0]) - 1
    columnOnes = nbOnesPerCol(lines, lineSize)

    half = len(lines) / 2
    energy = [0, 0]
    #energy[0] = epsilonRate, energy[1] = gammaRate
    
    rating = ["", ""]
    #rating[0] = 02, rating[1] = C02
    
    #lines kept for rating (0 -> 02, 1 -> C02)
    kept = [lines, lines]

    r = range(0, 2)

    #bit position for converting to decimal
    bitPosition = lineSize - 1
    for i in range(lineSize):

        #compute energy
        ones = columnOnes[i]
        energy[ones > half] += 2 ** bitPosition
        bitPosition -= 1

        for j in r:
            linesKept = len(kept[j])
            
            # if theres's still multiple lines kept
            if linesKept != 1:
                #recompute nbOnes from lines kept at column i
                localOne = nbOnesFromCol(kept[j], i)
                localHalf = linesKept / 2

                #check most/least common depending on j
                rating[j] += str(int(localOne >= localHalf)) if j == 0 else str(int(localOne < localHalf))
                #update lines kept
                kept[j] = [s for s in kept[j] if s.startswith(rating[j])]
            
            #if only one line, use as result and update range
            else: 
                rating[j] = kept[j][0]
                r = range(0, 1) if j == 1 else range(1, 2)
        

    print(energy[0] * energy[1])
    print(int(rating[0], 2) * int(rating[1], 2))

def main() -> None:
    exec("Day03/Day03.txt")

if __name__ == "__main__":
    main()