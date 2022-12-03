
from numpy import mat


def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    
    sumPart1 = 0
    sumPart2 = 0
    lineCount = 0
    group = set()
    for line in file.readlines():
        line = line.replace("\n", "")
        
        #Part 1
        half = int(len(line) / 2)
        in1, in2 = line[:half], line[half:]
        dupl = ord(set(in1).intersection(in2).pop())
        sumPart1 += (dupl - 97 if dupl >= 97 and dupl <= 122 else (dupl - 65) + 26) + 1
        
        #Part 2
        if (lineCount % 3 == 2):
            prio = ord(group.intersection(line).pop())
            sumPart2 += (prio - 97 if prio >= 97 and prio <= 122 else (prio - 65) + 26) + 1
        elif lineCount % 3 == 1:
            group = group.intersection(line)
        else:
            group = set(line)
        lineCount += 1

    print(sumPart1, sumPart2)

def main() -> None:
    exec("2023/Day03/Day03.txt")

if __name__ == "__main__":
    main()