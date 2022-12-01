def exec(fileName: str) -> None:

    field = [[0 for x in range(1000)] for y in range(1000)]
    
    file = open(fileName, "r")
    for line in file.readlines():
        points = line.split(" -> ")
        p = [eval("[" + x + "]") for x in points]
        
        start = p[0]
        end = p[1]

        incX = 1 if start[0] < end[0] else -1 if start[0] > end[0] else 0
        incY = 1 if start[1] < end[1] else -1 if start[1] > end[1] else 0

        # uncomment for vertical and horizontal only
        # if incX and incY:
        #     continue
        
        #weird condition to reach endPoint only if required
        while ((start[0] != end[0] and incX) or not incX) and ((start[1] != end[1] and incY) or not incY):
            field[start[1]][start[0]] += 1
            start[0] += incX
            start[1] += incY

        #include last point
        field[start[1]][start[0]] += 1
    
    counter = 0
    for line in field:
        for elem in line:
            if elem > 1:
                counter += 1

    print(counter)
def main() -> None:
    exec("Day05/Day05.txt")

if __name__ == "__main__":
    main()