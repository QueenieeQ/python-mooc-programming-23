# Write your solution here
def row_correct(matrix: list, row_no: int):
    # print(matrix)
    # count = 0
    # index = 0
    row = matrix[row_no]
    for num in range(1, 10):
        if row.count(num) > 1:
            return False
    return True
def row_correct2(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
