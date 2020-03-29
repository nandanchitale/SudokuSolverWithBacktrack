# Using backtracking algorithms

# Starting with an incomplete board:
# Find some empty space
# Attempt to place the digits 1-9 in that space
# Check if that digit is valid in the current spot based on the current board
#   a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
#   b. If it is not valid, reset the square you just filled and go back to the previous step.
# Once the board is full by the definition of this algorithm we have found a solution.


# Step 1: Pick empty square.
# Step 2: Try all the numbers.
# Step 3: Find one number that works.
# Step 4: Repeat
# Step 5: Backtrack ( using recursion)

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo) :
    find = find_empty(bo)
    if not find :
        return True
    else :
        row, col = find

    for i in range(1, 10) :
        if valid(bo, i, (row, col)) :
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def print_board(bo) :
    for i in range(len(bo)) :
        if i % 3 == 0 and i != 0 :
            print("----------------------------------")

        for j in range(len(bo[0])) :
            if j % 3 == 0 and j != 0 :
                print(" | ", end="")

            if j == 8 :
                print(bo[i][j])
            else :
                print(str(bo[i][j]) + "  ", end="")


def valid(bo, num, pos) :
    # Check row
    for i in range(len(bo[0])) :
        if bo[pos[0]][i] == num and pos[1] != i :
            return False

    # Check Columns
    for i in range(len(bo)) :
        if bo[i][pos[1]] == num and pos[0] != i :
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3) :
        for j in range(box_x * 3, box_x * 3 + 3) :
            if bo[i][j] == num and (i, j) != pos :
                return False

    return True


def find_empty(bo) :
    for i in range(len(bo)) :
        for j in range(len(bo[0])):
            if bo[i][j] == 0 :
                return (i, j)  # row, column

    return None

print("Before Solving...\n")
print_board(board)

print("\n\nAfter solving...\n")
solve(board)
print_board(board)
