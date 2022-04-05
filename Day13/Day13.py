from copy import deepcopy
import numpy

def fold(mat: numpy.array, index: int, axis: int) -> numpy.array:
    mat = numpy.delete(mat, index, axis)
    m1, m2 = numpy.split(mat, 2, axis)
    m2 = numpy.flip(m2, axis)
    return numpy.logical_or(m1, m2)

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    mat = numpy.zeros((10000, 10000), numpy.int8)

    instructions = []
    for line in file.readlines():
        line.replace("\n", "")
        if line.startswith("fold"):
            s = line.split(" ")[-1].split("=")
            instructions.append((0 if s[0] == "y" else 1, int(s[1])))
        
        elif not line.startswith("\n"):
            (c, r) = [int(x) for x in line.split(",")]
            mat[r][c] = True

    maxR = instructions[1][1] * 2 + 1
    maxC = instructions[0][1] * 2 + 1
    mat = mat[:maxR, :maxC]
    
    for axis, index in instructions:
        mat = fold(mat, index, axis)
        print(numpy.count_nonzero(mat))
    
    mat = numpy.array([["#" if v else "." for v in r] for r in mat])
    print(mat)
    for i in range(8):
        print(mat[:, i * 5:(i + 1) * 5])
    
def main() -> None:
    exec("Day13/Day13.txt")

if __name__ == "__main__":
    main()