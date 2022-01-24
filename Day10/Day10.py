from typing import List

openingMatch = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

closingMatch = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<"
}

CorruptionPoints = {
    ""  : 0,
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

IncompletePoints = {
    ""  : 0,
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

#return points of either a corrupted or incomplete line, or 0 otherwise
def getPoints(s: str) -> List[str]:
    stack = []

    #determine corrupted
    for c in s:
        if c in openingMatch.keys():
            stack.append(c)
        elif len(stack) and closingMatch[c] != stack[-1]:
            return [CorruptionPoints[c], 0]
        else:
            stack.pop()
    
    #determine incomplete
    if len(stack):
        pts = 0
        for c in reversed(stack):
            pts = pts * 5 + IncompletePoints[openingMatch[c]]
        return [0, pts]
    
    return [0, 0]

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    res = [0, []]
    for line in file.readlines():
        line = line.replace('\n', '')
        tmp = getPoints(line)
        res[0] += tmp[0]
        if tmp[1]:
            res[1].append(tmp[1])
    
    half = int(len(res[1]) / 2)
    res[1].sort()
    print(res[0], res[1][half])

def main() -> None:
    exec("Day10/Day10.txt")

if __name__ == "__main__":
    main()