
from numpy import mat
import re

def exec(fileName: str) -> None:
    
    file = open(fileName, "r")

    counterPart1 = 0
    counterPart2 = 0
    
    for line in file.readlines():
        
        line = line.replace("\n", "")
        input = [int(x) for x in re.split(r'[-,]', line)]

        if input[0] <= input[2] and input[3] <= input[1] or input[2] <= input[0] and input[1] <= input[3]:
            counterPart1 += 1

        if input[0] <= input[2] and input[2] <= input[1] or input[0] <= input[3] and input[3] <= input[1] \
            or input[2] <= input[0] and input[0] <= input[3] or input[2] <= input[1] and input[1] <= input[3]:
            counterPart2 += 1

    print(counterPart1, counterPart2)

def main() -> None:
    exec("2023/Day04/Day04.txt")

if __name__ == "__main__":
    main()