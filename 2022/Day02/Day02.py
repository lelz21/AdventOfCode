def exec(fileName: str) -> None:
    
    file = open(fileName, "r")
    pos = [0, 0, 0]
    lines = file.readlines()
    
    for line in lines:
        direction, magnitude = line.split()
        magnitude = int(magnitude)
        if direction == "forward":
            pos[0] += magnitude
            pos[1] += pos[2] * magnitude
        elif direction == "up":
            pos[2] -= magnitude
        else: #down
            pos[2] += magnitude

    print(pos[0] * pos[1])

def main() -> None:
    exec("Day02/Day02.txt")

if __name__ == "__main__":
    main()