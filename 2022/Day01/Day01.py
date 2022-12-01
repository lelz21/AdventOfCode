import sys

def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    count = [0, 0]
    lines = [int(x) for x in file.readlines()]
    
    for i in range(1, len(lines)):
        #Part 1 : increasing value
        if lines[i-1] < lines[i]:
            count[0] += 1

        #Part 2 : increasing 3-valued window
        if (i < len(lines) - 2):
            if sum(lines[i-1:i+2]) < sum(lines[i:i+3]):
                count[1] += 1
    
    print(count)

def main() -> None:
    exec("Day01/Day01.txt")

if __name__ == "__main__":
    main()