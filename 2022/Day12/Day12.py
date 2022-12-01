from collections import defaultdict
from copy import deepcopy


def nbPaths(graph: defaultdict(list), current: str, useTwice = False, usedTwice: str = "",
            visited: set = set(), path: list = [], verbose = False) -> int:
    i = 0

    visited = deepcopy(visited)
    path = deepcopy(path)
    
    if current.islower():
        visited.add(current)
    if verbose:
        path.append(current)

    for neighbour in graph[current]:
        if not neighbour in visited:
            if neighbour == "end":
                i += 1
                if verbose: 
                    path.append("end")
                    print("End Reached :", path)
            else:
                i += nbPaths(graph, neighbour, useTwice, usedTwice, visited, path, verbose)
        elif useTwice and neighbour != "start" and neighbour.islower() and not len(usedTwice):
            i += nbPaths(graph, neighbour, False, usedTwice, visited, path, verbose)

    return i

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    g = defaultdict(list)

    for line in file.readlines():
        v1, v2 = line.replace("\n", "").split("-")
        g[v1].append(v2)
        g[v2].append(v1)

    print(nbPaths(g, "start"))
    print(nbPaths(g, "start", True))

def main() -> None:
    exec("Day12/shortDay12.txt")

if __name__ == "__main__":
    main()