import copy

def exec(fileName: str) -> None:
    
    stacksPart1 = []
    if fileName.__contains__("short"):
        stacksPart1.append(["Z", "N"])
        stacksPart1.append(["M", "C", "D"])
        stacksPart1.append(["P"])
    else:
        stacksPart1.append(["S", "T", "H", "F", "W", "R"])
        stacksPart1.append(["S", "G", "D", "Q", "W"])
        stacksPart1.append(["B", "T", "W"])
        stacksPart1.append(["D", "R", "W", "T", "N", "Q", "Z", "J"])
        stacksPart1.append(["F", "B", "H", "G", "L", "V", "T", "Z"])
        stacksPart1.append(["L", "P", "T", "C", "V", "B", "S", "G"])
        stacksPart1.append(["Z", "B", "R", "T", "W", "G", "P"])
        stacksPart1.append(["N", "G", "M", "T", "C", "J", "R"])
        stacksPart1.append(["L", "G", "B", "W"])
        
    stacksPart2 = copy.deepcopy(stacksPart1)

    file = open(fileName, "r")
    
    if stacksPart1 and stacksPart2:
        for line in file.readlines():
            line = line.replace("\n", "")
            _, num, _, start, _, end  = [int(x) if x.isnumeric() else 0 for x in line.split(" ")]
            for i in range(num):
                stacksPart1[end - 1].append(stacksPart1[start - 1].pop())
            
            tmp = []
            for i in range(num):
                tmp.append(stacksPart2[start - 1].pop())
            
            for i in range(num):
                stacksPart2[end - 1].append(tmp.pop())

    
    for stack in stacksPart1:
        print(stack.pop(), end="")
    print("")
    for stack in stacksPart2:
        print(stack.pop(), end="")

def main() -> None:
    exec("2023/Day05/Day05.txt")

if __name__ == "__main__":
    main()