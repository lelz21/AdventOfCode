from typing import List
import statistics
from math import comb    
import sys

def dist(n1: int, n2: int) -> int:
    return comb(abs(n1 - n2) + 1, 2)

def exec(fileName: str) -> None:
    file = open(fileName, "r")
    l = [int(x) for x in file.readline().split(",")]

    med = statistics.median(l)
    mean = statistics.mean(l)

    s = 0
    min = sys.maxsize
    max = 0
    for elem in l:
        s += abs(elem - med)
        min = min if min < elem else elem
        max = max if max > elem else elem
    
    print(s)

    r = range(min, max)
    min = sys.maxsize
    for i in r:
        s = 0
        for elem in l:
            s += comb(abs(i - elem) + 1, 2)
        min = min if min < s else s
    
    print(min)

def main() -> None:
    exec("Day07/Day07.txt")

if __name__ == "__main__":
    main()