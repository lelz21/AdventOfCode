from collections import deque

def allDifferent(q: deque) -> bool:
    tmp = q.copy()
    kwown = set()
    while tmp:
        char = tmp.popleft()
        if not char in kwown:
            kwown.add(char)
        else:
            return False
    return True

def checkDistinctAfter(msg: str, n: int) -> int:
    q = deque()
    index = 0
    found = False

    while index < len(msg) and not found:

        q.append(msg[index])
        if index > n - 1:
            found = allDifferent(q)
            q.popleft()
    
        index += 1
    return index - 1

def exec(fileName: str) -> None:

    file = open(fileName, "r")

    for line in file.readlines():
        line.replace("\n", "")
        
        print(checkDistinctAfter(line, 4))
        print(checkDistinctAfter(line, 14))

def main() -> None:
    exec("2023/Day06/Day06.txt")

if __name__ == "__main__":
    main()