from collections import defaultdict, deque
from turtle import right

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    #initial polymer
    initial = file.readline().replace("\n", "")

    #start counting ocurrences and pairs
    occurrences = defaultdict(int)
    pairOcurrences = defaultdict(int)
    for i in range(len(initial)):
        current = initial[i]
        occurrences[current] += 1
        if i < len(initial) - 1:
            next = initial[i + 1]
            pairOcurrences[current + next] += 1

    #skip empty line
    file.readline()

    #create dict of insertion rules
    rules = {}
    for line in file.readlines():
        key, value = line.replace("\n", "").split(" -> ")
        rules[key] = value
    
    # number of iterations
    for i in range(40):
        #new dict of next pairs
        tmp = defaultdict(int)
        #iterate trought current pairs
        for key, value in pairOcurrences.items():
            #rules result, left and right pairs
            res = rules[key]
            left = key[0] + res
            right = res + key[1]

            #keep track of occurrences
            occurrences[res] += value

            #add values to next pairs
            tmp[left] += value
            tmp[right] += value

        #update pairs for next iteration
        pairOcurrences = tmp

    #compute min and max of values
    lower = min(occurrences.values())
    upper = max(occurrences.values())

    #print max - min
    print(upper - lower)
    
def main() -> None:
    exec("Day14/Day14.txt")

if __name__ == "__main__":
    main()