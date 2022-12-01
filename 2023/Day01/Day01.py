def top(current: list, new: int) -> list:

    if current[0] < new:
        current[2] = current[1]
        current[1] = current[0]
        current[0] = new

    elif current[1] < new:
        current[2] = current[1]
        current[1] = new

    elif current[2] < new:
        current[2] = new

    return current

def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    maximum = [0, 0, 0]
    count = 0
    for x in file.readlines():
        if x == "\n":
            maximum = top(maximum, count)
            count = 0
        else:
            count += int(x)
        
    print(maximum[0])
    print(sum(maximum))

def main() -> None:
    exec("2023/Day01/Day01.txt")

if __name__ == "__main__":
    main()