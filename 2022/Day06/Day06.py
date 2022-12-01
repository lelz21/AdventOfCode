from typing import List

def megaShift(l: List[int]) -> None:
    l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8] = l[1], l[2], l[3], l[4], l[5], l[6], l[7] + l[0], l[8], l[0]

def exec(fileName: str) -> None:
    file = open(fileName, "r")
    lanterfishes = [int(x) for x in file.readline().split(',')]

    lut = [0] * 9

    for lanterfish in lanterfishes:
        lut[lanterfish] += 1
    
    for i in range(256):
        megaShift(lut)
    print(sum(lut))

def main() -> None:
    exec("Day06/Day06.txt")

if __name__ == "__main__":
    main()