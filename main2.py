import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]

rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵" or gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print("  ", end=" |")
    print("\n   +----+----+----+----+----+----+----+")


def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn


def checkForWinner(chip):
    # Check horizontal spaces
    for y in range(rows):
        for x in range(cols - 3):
            if gameBoard[y][x] == chip and gameBoard[y][x + 1] == chip and gameBoard[y][x + 2] == chip and gameBoard[y][x + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical spaces
    for x in range(cols):
        for y in range(rows - 3):
            if gameBoard[y][x] == chip and gameBoard[y + 1][x] == chip and gameBoard[y + 2][x] == chip and gameBoard[y + 3][x] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper right to bottom left diagonal spaces
    for x in range(cols - 3):
        for y in range(3, rows):
            if gameBoard[y][x] == chip and gameBoard[y - 1][x + 1] == chip and gameBoard[y - 2][x + 2] == chip and gameBoard[y - 3][x + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper left to bottom right diagonal spaces
    for x in range(cols - 3):
        for y in range(rows - 3):
            if gameBoard[y][x] == chip and gameBoard[y + 1][x + 1] == chip and gameBoard[y + 2][x + 2] == chip and gameBoard[y + 3][x + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False


def coordinateParser(inputString):
    coordinate = [None] * 2
    if inputString[0] == "A":
        coordinate[1] = 0
    elif inputString[0] == "B":
        coordinate[1] = 1
    elif inputString[0] == "C":
        coordinate[1] = 2
    elif inputString[0] == "D":
        coordinate[1] = 3
    elif inputString[0] == "E":
        coordinate[1] = 4
    elif inputString[0] == "F":
        coordinate[1] = 5
    elif inputString[0] == "G":
        coordinate[1] = 6
    else:
        print("Invalid column")
        return None

    coordinate[0] = int(inputString[1])
    if coordinate[0] < 0 or coordinate[0] >= rows:
        print("Invalid row")
        return None
    return coordinate


def isSpaceAvailable(intendedCoordinate):
    return gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == ""


def gravityChecker(intendedCoordinate):
    # Calculate space below
    spaceBelow = [intendedCoordinate[0] + 1, intendedCoordinate[1]]
    # Is the coordinate at ground level
    if spaceBelow[0] == rows:
        return True
    # Check if there's a token below
    if not isSpaceAvailable(spaceBelow):
        return True
    return False


leaveLoop = False
turnCounter = 0
while not leaveLoop:
    if turnCounter % 2 == 0:
        printGameBoard()
        while True:
            spacePicked = input("\nChoose a space (e.g., A0): ").upper()
            coordinate = coordinateParser(spacePicked)
            if coordinate and isSpaceAvailable(coordinate) and gravityChecker(coordinate):
                modifyArray(coordinate, '🔵')
                break
            else:
                print("Not a valid coordinate, please try again.")
        winner = checkForWinner('🔵')
    else:
        while True:
            cpuChoice = [random.choice(possibleLetters), random.randint(0, rows - 1)]
            cpuCoordinate = coordinateParser(cpuChoice[0] + str(cpuChoice[1]))
            if cpuCoordinate and isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate):
                modifyArray(cpuCoordinate, '🔴')
                break
        winner = checkForWinner('🔴')

    if winner:
        printGameBoard()
        break

    turnCounter += 1
