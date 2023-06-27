def row_correct(matrix: list, row_no: int):
    # print(matrix)
    # count = 0
    # index = 0
    # print(matrix)
    row = matrix[row_no]
    for num in range(1, 10):
        if row.count(num) > 1:
            # print("error at ", row)
            return False
    return True
def column_correct(sudoku: list, column_no: int):
    # column = sudoku[column_no]
    # print(range(1,10))
    # column= []
    # for row in sudoku:
    #     column.append(row)
    #     # column = row[column_no]
    # for row in sudoku:
    #     column = row[column_no]
    #     print(column)
    column = [row[column_no] for row in sudoku]
    for num in range(1, 10):
        if column.count(num) > 1:
            return False
    return True
def block_correct(sudoku: list, row_no: int, column_no:int):
    block = []
    # print(sudoku)
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no +3):
            block.append(sudoku[i][j])
    # print(block)
    for number in range(1,10):
        if block.count(number)> 1:
            return False
        return True# Write your solution here
def sudoku_grid_correct(sudoku: list):
    for row in range(9):
        row_correct(sudoku, row)
        # if not row_correct(sudoku, row):
        #     print("Error: Incorrect row at index", row)
    for column in range(9):
        # print(sudoku[[1][0]])
        column_correct(sudoku, column)
        # if not row_correct(sudoku, column):
        #     print("Error: Incorrect row at index", column)
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            block_correct(sudoku, row, column)
    if row_correct == True and column_correct == True and block_correct == True:
        # print("Correct") 
        return True
    else:
        # print("Error")
        return False

# if __name__ == "__main__":
#     sudoku = [
#   [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
#   [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
#   [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
#   [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
#   [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
#   [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
#   [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
#   [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
#   [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
# ]
# sudoku_grid_correct(sudoku)