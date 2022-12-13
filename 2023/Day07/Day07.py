from __future__ import annotations

class Tree:
    def __init__(self, parent: Tree = None, name: str = "", size: int = 0) -> None:
        self.children = {}
        self.parent = parent
        self.name = name
        self.size = size

    def atMost(self, most: int = 100000) -> list:
        dirs = []
        if self.size < most and len(self.children):
            dirs.append(self.size)

        for child in self.children.values():
            dirs.extend(child.atMost(most))
        return dirs
    
    def atLeast(self, least: int = 100000) -> list:
        dirs = []
        if self.size > least and len(self.children):
            dirs.append(self.size)

        for child in self.children.values():
            dirs.extend(child.atLeast(least))
        return dirs
    
    def updateSize(self) -> None:
        for child in self.children.values():
            child.updateSize()
            self.size += child.size
    
    def as_str(self, depth = 0, indent = 4) -> str:
        ret = ["{}{}".format(" "*(indent * depth), "- " + self.name + (" (dir, " if len(self.children) else " (file, ") + "size = " + str(self.size) + ")")]
        for child in self.children.values():
            ret.append(child.as_str(depth + 1, indent))

        return "\n".join(ret)
        
    def __str__(self) -> str:
        return self.as_str()

def exec(fileName: str) -> None:

    file = open(fileName, "r")

    home = Tree(None, "/")
    current = home

    read = False

    for line in file.readlines():
        line = line.replace("\n", "").split(" ")
        if len(line) > 1:
            if line[0] == "$":
                read = False
                if line[1] == "cd":
                    if line[2] == "/":
                        current = home
                    elif line[2] == "..":
                        current = current.parent
                    else:
                        current = current.children[line[2]]
                else:
                    read = True
            elif read and len(line) == 2:
                if not line[1] in current.children:
                    current.children[line[1]] = Tree(current, line[1])
                    if line[0] != "dir":
                        current.children[line[1]].size = int(line[0])
    
    home.updateSize()
    # print(home)
    print(sum(home.atMost()))

    total = 70000000
    needed = 30000000
    used = home.size
    free = total - used
    target = needed - free
    print(min(home.atLeast(target)))

def main() -> None:
    exec("2023/Day07/Day07.txt")

if __name__ == "__main__":
    main()