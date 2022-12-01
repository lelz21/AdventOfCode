from typing import List, Tuple

#determine 5 and 2 from 6's shape by elimination
def determineVeryHard(s: str, decrypt: dict[int, str]) ->None:
    abc = "".join(sorted(s))
    size = len(s)

    if size == 5 and abc not in decrypt.values():
        if all([c in decrypt[6] for c in abc]):
            decrypt[5] = abc
        else:
            decrypt[2] = abc

#determine 0 and 6 from 7's shape by elimination
def determineHard(s: str, decrypt: dict[int, str]) -> None:
    abc = "".join(sorted(s))
    size = len(s)

    if size == 6 and abc not in decrypt.values():
        if all([c in abc for c in decrypt[7]]):
            decrypt[0] = abc
        else:
            decrypt[6] = abc

#determine 3 from 7's shape and 9 from 4's shape
def determineNotSoEasy(s: str, decrypt: dict[int, str]) -> None:
    abc = "".join(sorted(s))
    size = len(s)

    if abc not in decrypt.values():
        if size == 5:
            if all([c in abc for c in decrypt[7]]):
                decrypt[3] = abc
        elif size == 6:
            if all([c in abc for c in decrypt[4]]):
                decrypt[9] = abc

#determine the easiest segments from their size (1, 7, 4 and 8)
def determineEasy(s: str, decrypt: dict[int, str]) -> None:
    abc = "".join(sorted(s))
    size = len(s)

    options = { 2: 1, 3: 7, 4: 4, 7: 8 }
    if size in options:
        decrypt[options[size]] = abc

#decrypt input from 4 different methods called one after another
def decryptInput(input: List[str]) -> dict[int, str]:
    decrypt = {}
    functions = [
        determineEasy,
        determineNotSoEasy,
        determineHard,
        determineVeryHard
    ]
    for f in functions:
        for s in input.split():
            f(s, decrypt)
    return decrypt

#decrypt output from input
def decryptOutput(decrypt: dict[str, int], output: List[str]) -> List[int]:
    tmp = [0, 0]
    for s in output.split():
            abc = "".join(sorted(s))
            size = len(s)
        
            tmp[0] = tmp[0] * 10 + decrypt[abc]
            if size > 1 and size < 5 or size == 7:
                tmp[1] += 1
    return tmp

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    lines = [s for s in file.readlines()]

    counter = 0
    res = 0
    for line in lines:
        input = line.split(" | ")[0]
        output = line.split(" | ")[1]
        
        #decrypt input
        decrypt = decryptInput(input)
        
        #invert keys and values of decryption for easier manipulation on output decrypt
        decrypt = { v: k for k, v in decrypt.items() }

        #decrypt output from input
        tmp = decryptOutput(decrypt, output)

        res += tmp[0]
        counter += tmp[1]
    
    print(counter)
    print(res)

def main() -> None:
    exec("Day08/Day08.txt")

if __name__ == "__main__":
    main()