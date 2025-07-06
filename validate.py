from util import boxes
def validate(d):
    # Convert input string to a list of integers
    d = list(map(int, d))

    # Check rows
    for i in range(9):
        if not is_valid_group(d[i*9:(i+1)*9]):
            return False

    # Check columns
    for i in range(9):
        if not is_valid_group(d[i::9]):
            return False

    # Check boxes
    for i in range(3):
        for j in range(3):
            box_key = (i, j)
            if not is_valid_group([d[x] for x in boxes[box_key]]):
                return False

    return True
def is_valid_group(group):
    seen = set()
    for num in group:
        if num != 0:
            if num in seen or not (1 <= num <= 9):
                return False
            seen.add(num)
    return True
