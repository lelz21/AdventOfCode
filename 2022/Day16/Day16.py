from typing import Tuple
from math import prod

#map operations
map = {
    0 : sum,
    1 : prod,
    2 : min,
    3 : max,
    5 : lambda l : l[0] > l[1],
    6 : lambda l : l[0] < l[1],
    7 : lambda l : l[0] == l[1]
}

def readOperator(head: str) -> Tuple[int, int, int]:
    #read Header
    packetVersion = head[:3]
    packetID = int(head[3:6], 2)
    lengthTypeID = head[6:7]

    #trim Header
    head = head[7:]

    #read LengthTypeID
    lengthTypeID = 15 if lengthTypeID == "0" else 11
    length = int(head[:lengthTypeID], 2)
    head = head[lengthTypeID:]

    #intialization of loop paramters
    counter = 0
    lPacket = 7
    localSum = int(packetVersion, 2)
    results = []
    while counter < length:
        #read subHeader
        subPacketVersion = head[:3]
        subPacketID = head[3:6]

        #read packet
        if subPacketID == "100":
            result, count, loc = readLiteral(head)
        else:
            result, count, loc = readOperator(head)
        
        #update parameters
        localSum += loc
        head = head[count:]
        counter += count if lengthTypeID == 15 else 1
        lPacket += count
        results.append(result)

    #do operation
    result = map[packetID](results)

    # return length of packet and local sum of versions
    return [result, lPacket + lengthTypeID, localSum]


def readLiteral(head: str) -> Tuple[str, int, int]:
    #read header
    packetVersion = head[:3]
    packetID = head[3:6]

    #trim header
    head = head[6:]
    
    #initialize loop parameters
    length = 6
    stop = False
    result = ""
    #read literal
    while not stop:
        if head[0] != "1":
            stop = True
        result += head[1:5]
        head = head[5:]
        length += 5

    #return ressult, packetLength and packet version
    return [int(result, 2), length, int(packetVersion, 2)]

def exec(fileName: str) -> None:
    file = open(fileName, "r")

    line = file.readline().replace("\n", "")
    b = bin(int(line, 16))[2:].zfill(len(line) * 4)

    #read header
    packetVersion = b[:3]
    packetID = b[3:6]

    versionNumberSum = 0
    if packetID == "100":
        result, _, versionNumberSum = readLiteral(b)
    else:
        result, _, versionNumberSum = readOperator(b)
    
    print(versionNumberSum, result)

def main() -> None:
    exec("Day16/Day16.txt")

if __name__ == "__main__":
    main()