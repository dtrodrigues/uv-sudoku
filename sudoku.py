import sys
import subprocess
from util import boxes, intToBox, BASE_NAME

def printBoard(data):
    for i in range(0,9):
        for j in range(0,9):
            print(data[i*9+j], end=' ')
        print()

def solve(data):
    deplist = set()
    i, j = 0, 0
    for digit in data:
        if digit == '0':
            deplist.add(f"{BASE_NAME}_{i+1}{j+1}")

            for x in range(0,9):
                otherDigit = data[x*9+j]
                if otherDigit != '0':
                    deplist.add(f"{BASE_NAME}_{i+1}{j+1}!={otherDigit}")

            for x in range(0,9):
                otherDigit = data[i*9+x]
                if  otherDigit != '0':
                    deplist.add(f"{BASE_NAME}_{i+1}{j+1}!={otherDigit}")

            myPos = i*9+j
            box = intToBox[myPos]
            for x in boxes[box]:
                otherDigit = data[x]
                if otherDigit != '0':
                    deplist.add(f"{BASE_NAME}_{i+1}{j+1}!={otherDigit}")

        else:
            deplist.add(f"{BASE_NAME}_{i+1}{j+1}=={digit}")
        
        j += 1
        if j == 9:
            j = 0
            i += 1

    proc = subprocess.run(
        ["uv", "pip", "compile", "-", "--no-index", "--find-links", "wheels/", "-q", "--no-header", "--no-annotate"],
        input="\n".join(deplist),
        text=True,
        capture_output=True
    )

    # sort the output requirements and then return the joined last characters (version numbers) of each line
    return ''.join(line[-1] for line in sorted(proc.stdout.splitlines()))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 sudoku.py <input_data>")
        sys.exit(1)
    inp = sys.argv[1]
    if len(inp) == 81:
        printBoard(solve(inp))
    else:
        print("Input must be a string of 81 digits representing the Sudoku puzzle.")
        sys.exit(1)
